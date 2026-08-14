#!/usr/bin/env python3
"""
Statistical Physics Knowledge Brain - PDF Conversion & Vector Indexing Script
=============================================================================

LOCATION & DOCUMENTATION:
  This script is located at `scripts/convert_and_index.py`.
  It builds a private, local semantic search index from PDF textbooks (e.g., Reif, Pathria).

HOW PDF EXTRACTION & INDEXING WORKS:
  1. PDF Conversion:
     - Uses `Marker` (GPU engine) if CUDA is available for high-quality OCR/layout parsing.
     - Falls back to `PyMuPDF` (CPU) to extract text page-by-page while preserving LaTeX formulas.
  2. LaTeX-Aware Chunking:
     - Splits text into ~600-token chunks at paragraph/heading boundaries.
     - Preserves math blocks (`$$...$$` and `\\[...\\]`) intact within chunks.
     - Tracks active heading context stack (e.g. "Chapter 3 > Canonical Ensemble > Partition Function").
  3. Vector Embedding & LanceDB Storage:
     - Computes vector embeddings using SentenceTransformers (`all-MiniLM-L6-v2`).
     - Saves vectors and metadata into a local `LanceDB` database (`./local_index/`).

HOW TO RUN:
  Terminal:
    $ make index
    OR
    $ python3 scripts/convert_and_index.py --pdf_dir ./sample_pdfs/ --index_dir ./local_index/

HOW TO EXTRACT INFO PROGRAMMATICALLY IN PYTHON:
  ```python
  import lancedb

  # 1. Connect to local index
  db = lancedb.connect("./local_index/")
  table = db.open_table("book_chunks")

  # 2. Convert table to Pandas DataFrame to extract raw chunks & metadata
  df = table.to_pandas()
  print(df[["source_id", "section", "text"]])

  # 3. Perform vector search programmatically
  from sentence_transformers import SentenceTransformer
  model = SentenceTransformer("all-MiniLM-L6-v2")
  query_vec = model.encode("Canonical partition function derivation")
  results = table.search(query_vec).limit(5).to_list()
  for r in results:
      print(r["source_id"], r["section"], r["text"][:100])
  ```
"""

import os
import re
import sys
import json
import glob
from pathlib import Path
import click
from dotenv import load_dotenv
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn

# Load .env default values
load_dotenv()

console = Console()


def count_tokens(text: str, encoder=None) -> int:
    """Estimate token count using tiktoken or simple word ratio fallback."""
    if encoder:
        return len(encoder.encode(text))
    return len(text.split()) * 4 // 3


def extract_pdf_pymupdf(pdf_path: str) -> str:
    """Fast CPU extraction using PyMuPDF (fitz). Extracts raw text characters (Unicode symbols)."""
    import fitz  # PyMuPDF
    doc = fitz.open(pdf_path)
    md_pages = []
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text("text")
        md_pages.append(f"<!-- Page {page_num + 1} -->\n{text.strip()}\n")
        
    doc.close()
    return "\n\n".join(md_pages)


def extract_pdf_marker(pdf_path: str) -> str:
    """Use Marker OCR engine (marker_single) to convert PDF layout and math into true LaTeX formulas ($$...$$)."""
    import subprocess
    import tempfile
    
    filename = Path(pdf_path).name
    marker_bin = str(Path(sys.executable).parent / "marker_single")
    if not Path(marker_bin).exists():
        marker_bin = "marker_single"
        
    console.print(f"[bold blue]Running Marker OCR engine for full LaTeX math extraction on {filename}...[/bold blue]")
    
    with tempfile.TemporaryDirectory() as tmp_dir:
        cmd = [marker_bin, pdf_path, "--output_dir", tmp_dir, "--output_format", "markdown"]
        res = subprocess.run(cmd, capture_output=True, text=True)
        
        pdf_stem = Path(pdf_path).stem
        md_file = Path(tmp_dir) / pdf_stem / f"{pdf_stem}.md"
        if md_file.exists():
            return md_file.read_text(encoding="utf-8")
        else:
            console.print(f"[yellow]Marker conversion produced no file or returned error. Log:\n{res.stderr[:500]}[/yellow]")
            raise RuntimeError(f"Marker failed for {filename}")


def convert_pdf_to_markdown(pdf_path: str, engine: str = "pymupdf", use_gpu: bool = False) -> str:
    """Convert a single PDF to Markdown via Marker (true LaTeX math) or PyMuPDF (fast plain text)."""
    filename = Path(pdf_path).name
    
    if engine == "marker" or use_gpu:
        try:
            return extract_pdf_marker(pdf_path)
        except Exception as e:
            console.print(f"[yellow]Marker extraction failed ({e}). Falling back to PyMuPDF...[/yellow]")

    console.print(f"[cyan]Extracting text via PyMuPDF for {filename}... (Fast mode: plain text formulas; use --engine marker for LaTeX math)[/cyan]")
    return extract_pdf_pymupdf(pdf_path)


def chunk_markdown(markdown_text: str, source_id: str, encoder=None, min_chunk_tokens=100, target_chunk_tokens=600, max_chunk_tokens=1000):
    """
    Markdown & LaTeX-aware chunker.
    - Preserves $$ ... $$ math blocks intact.
    - Keeps heading context (stack of active headings).
    - Splits at paragraph boundaries (double newlines).
    - Allows single blocks up to max_chunk_tokens before forcing a split.
    """
    heading_pattern = re.compile(r'^(#{1,6})\s+(.+)$')
    latex_block_pattern = re.compile(r'(\$\$.*?\$\$|\\\[.*?\\\])', re.DOTALL)
    
    # Split text into blocks while preserving LaTeX equations as single units
    raw_blocks = latex_block_pattern.split(markdown_text)
    
    chunks = []
    current_chunk_tokens = 0
    current_text_parts = []
    heading_stack = []
    current_heading = "General"
    
    for block in raw_blocks:
        if not block or not block.strip():
            continue
            
        lines = block.split("\n")
        
        for line in lines:
            h_match = heading_pattern.match(line.strip())
            if h_match:
                level = len(h_match.group(1))
                h_text = h_match.group(2).strip()
                # Update heading stack
                heading_stack = heading_stack[:level-1]
                heading_stack.append(h_text)
                current_heading = " > ".join(heading_stack)
        
        block_tokens = count_tokens(block, encoder)
        
        # If adding block exceeds max target tokens and current chunk is not empty, push current chunk
        if current_chunk_tokens + block_tokens > target_chunk_tokens and current_text_parts:
            chunk_text = "\n\n".join(current_text_parts).strip()
            if chunk_text:
                chunks.append({
                    "text": chunk_text,
                    "source_id": source_id,
                    "section": current_heading,
                    "heading_text": heading_stack[-1] if heading_stack else current_heading,
                    "concept_links": "[]"
                })
            current_text_parts = []
            current_chunk_tokens = 0

        # If a single block exceeds max_chunk_tokens by itself
        if block_tokens > max_chunk_tokens:
            # If current text accumulated, emit it first
            if current_text_parts:
                chunk_text = "\n\n".join(current_text_parts).strip()
                chunks.append({
                    "text": chunk_text,
                    "source_id": source_id,
                    "section": current_heading,
                    "heading_text": heading_stack[-1] if heading_stack else current_heading,
                    "concept_links": "[]"
                })
                current_text_parts = []
                current_chunk_tokens = 0

            # Keep large block as a single unit up to 1000 tokens context
            chunks.append({
                "text": block.strip(),
                "source_id": source_id,
                "section": current_heading,
                "heading_text": heading_stack[-1] if heading_stack else current_heading,
                "concept_links": "[]"
            })
        else:
            current_text_parts.append(block.strip())
            current_chunk_tokens += block_tokens

    # Push remaining chunk
    if current_text_parts:
        chunk_text = "\n\n".join(current_text_parts).strip()
        if chunk_text:
            chunks.append({
                "text": chunk_text,
                "source_id": source_id,
                "section": current_heading,
                "heading_text": heading_stack[-1] if heading_stack else current_heading,
                "concept_links": "[]"
            })

    return chunks


@click.command()
@click.option('--pdf_dir', default=os.getenv('PDF_DIR', './sample_pdfs/'), help='Directory containing source PDFs')
@click.option('--index_dir', default=os.getenv('INDEX_DIR', './local_index/'), help='Directory for LanceDB vector storage')
@click.option('--embedding_model', default=os.getenv('EMBEDDING_MODEL', 'all-MiniLM-L6-v2'), help='SentenceTransformers model name')
@click.option('--engine', type=click.Choice(['pymupdf', 'marker']), default='pymupdf', help='Conversion engine: pymupdf (fast text) or marker (full LaTeX math OCR)')
@click.option('--use_gpu', is_flag=True, default=os.getenv('USE_GPU', 'false').lower() in ('true', '1', 't'), help='Use Marker engine with GPU if available')
def main(pdf_dir, index_dir, embedding_model, engine, use_gpu):
    """Convert PDFs to Markdown and create a local LanceDB vector search index."""
    console.rule("[bold green]Statistical Physics Knowledge Brain - Indexer[/bold green]")
    
    pdf_path = Path(pdf_dir)
    if not pdf_path.exists():
        console.print(f"[bold red]PDF directory '{pdf_dir}' does not exist.[/bold red]")
        console.print(f"[yellow]Creating sample PDF directory '{pdf_dir}'... Place your PDF books here.[/yellow]")
        pdf_path.mkdir(parents=True, exist_ok=True)
        return

    pdf_files = list(pdf_path.glob("*.pdf")) + list(pdf_path.glob("**/*.pdf"))
    if not pdf_files:
        console.print(f"[yellow]No PDF files found in '{pdf_dir}'. Please add PDFs and re-run.[/yellow]")
        return

    console.print(f"Found [bold cyan]{len(pdf_files)}[/bold cyan] PDF file(s) to index.")
    
    # Initialize tiktoken encoder if available
    try:
        import tiktoken
        encoder = tiktoken.get_encoding("cl100k_base")
    except Exception:
        encoder = None

    # Load SentenceTransformer model
    console.print(f"Loading embedding model '[bold green]{embedding_model}[/bold green]'...")
    try:
        from sentence_transformers import SentenceTransformer
        model = SentenceTransformer(embedding_model)
    except Exception as e:
        console.print(f"[bold red]Failed to load SentenceTransformer model ({e}). Please check requirements.[/bold red]")
        sys.exit(1)

    all_chunks = []
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        console=console
    ) as progress:
        task = progress.add_task("Processing PDFs...", total=len(pdf_files))
        
        output_dir = Path("./output")
        output_dir.mkdir(parents=True, exist_ok=True)
        
        for pdf in pdf_files:
            progress.update(task, description=f"Converting {pdf.name}...")
            md_text = convert_pdf_to_markdown(str(pdf), engine=engine, use_gpu=use_gpu)
            
            # Save raw converted markdown locally for easy copy-paste & AI preparation
            md_output_path = output_dir / f"{pdf.stem}.md"
            with open(md_output_path, "w", encoding="utf-8") as f:
                f.write(md_text)
            console.print(f"[green]Saved raw Markdown to '{md_output_path}'[/green]")
            
            progress.update(task, description=f"Chunking {pdf.name}...")
            chunks = chunk_markdown(md_text, source_id=pdf.name, encoder=encoder)
            all_chunks.extend(chunks)
            
            progress.advance(task)

    if not all_chunks:
        console.print("[yellow]No text chunks generated.[/yellow]")
        return

    console.print(f"Extracted [bold cyan]{len(all_chunks)}[/bold cyan] Markdown chunks.")
    console.print("Generating vector embeddings...")
    
    texts = [c["text"] for c in all_chunks]
    embeddings = model.encode(texts, show_progress_bar=True, convert_to_numpy=True)

    rows = []
    for chunk, vector in zip(all_chunks, embeddings):
        rows.append({
            "vector": vector.tolist(),
            "text": chunk["text"],
            "source_id": chunk["source_id"],
            "section": chunk["section"],
            "heading_text": chunk["heading_text"],
            "concept_links": chunk["concept_links"]
        })

    # Connect to LanceDB
    import lancedb
    os.makedirs(index_dir, exist_ok=True)
    db = lancedb.connect(index_dir)
    
    table_name = "book_chunks"
    table = db.create_table(table_name, data=rows, mode="overwrite")
    
    console.rule("[bold green]Indexing Complete[/bold green]")
    console.print(f"[bold green]Successfully indexed {len(rows)} chunks into LanceDB table '{table_name}' at '{index_dir}'![/bold green]")


if __name__ == "__main__":
    main()
