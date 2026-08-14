#!/usr/bin/env python3
"""
Statistical Physics Knowledge Brain - CLI Semantic Query Tool
============================================================

LOCATION & DOCUMENTATION:
  This script is located at `scripts/query_local.py`.
  It performs vector similarity searches against indexed textbook PDFs in LanceDB.

HOW QUERY EXTRACTION WORKS:
  1. Loads user query string (e.g. "Bose-Einstein condensation transition temperature").
  2. Embeds the query using SentenceTransformers (`all-MiniLM-L6-v2`).
  3. Searches `local_index/` (LanceDB table `book_chunks`) for nearest vector neighbors.
  4. Returns the top `k` matching text chunks along with source PDF name, heading section, and distance metric.

HOW TO RUN:
  Terminal:
    $ make query
    OR
    $ python3 scripts/query_local.py "Bose Einstein Condensation" --top_k 5

PROGRAMMATIC EXTRACTION IN YOUR OWN CODE / NOTEBOOKS:
  ```python
  from scripts.query_local import main
  import lancedb
  from sentence_transformers import SentenceTransformer

  # Connect to index
  db = lancedb.connect("./local_index/")
  table = db.open_table("book_chunks")

  # Embed query
  model = SentenceTransformer("all-MiniLM-L6-v2")
  query_vector = model.encode("Equivalence of canonical and microcanonical ensembles")

  # Query top 3 matching chunks
  results = table.search(query_vector).limit(3).to_list()
  for item in results:
      print(f"Source: {item['source_id']} | Section: {item['section']}")
      print(item['text'])
      print("-" * 50)
  ```
"""

import os
import sys
import click
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel

load_dotenv()
console = Console()

@click.command()
@click.argument('query', required=False)
@click.option('--index_dir', default=os.getenv('INDEX_DIR', './local_index/'), help='LanceDB storage directory')
@click.option('--embedding_model', default=os.getenv('EMBEDDING_MODEL', 'all-MiniLM-L6-v2'), help='SentenceTransformers model name')
@click.option('--top_k', default=5, help='Number of top results to return')
def main(query, index_dir, embedding_model, top_k):
    """Query the local PDF vector index."""
    if not query:
        query = click.prompt("Enter search query")

    if not os.path.exists(index_dir):
        console.print(f"[bold red]Index directory '{index_dir}' not found. Please run 'make index' first.[/bold red]")
        sys.exit(1)

    import lancedb
    from sentence_transformers import SentenceTransformer

    console.print(f"Connecting to index at '[cyan]{index_dir}[/cyan]'...")
    db = lancedb.connect(index_dir)

    try:
        table = db.open_table("book_chunks")
    except Exception as e:
        console.print(f"[bold red]Could not open table 'book_chunks' in '{index_dir}'. Run indexing first. ({e})[/bold red]")
        sys.exit(1)

    console.print(f"Embedding query using '[green]{embedding_model}[/green]'...")
    model = SentenceTransformer(embedding_model)
    query_vec = model.encode(query).tolist()

    results = table.search(query_vec).limit(top_k).to_list()

    console.rule(f"[bold green]Search Results for: '{query}'[/bold green]")

    if not results:
        console.print("[yellow]No matching results found.[/yellow]")
        return

    for i, res in enumerate(results, start=1):
        source = res.get("source_id", "Unknown")
        section = res.get("section", "General")
        text = res.get("text", "").strip()
        score = res.get("_distance", 0.0)

        title = f"[bold cyan]Result #{i}[/bold cyan] | Source: [yellow]{source}[/yellow] | Section: [magenta]{section}[/magenta] (Dist: {score:.4f})"
        console.print(Panel(text, title=title, border_style="blue"))


if __name__ == "__main__":
    main()
