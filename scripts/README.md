# 🛠️ Python Indexing & Vector Search Scripts

This directory contains the Python RAG (Retrieval-Augmented Generation) indexing and query pipeline for extracting info and searching local physics textbook PDFs (e.g. Reif 1968, Pathria & Beale 2021).

---

## 📁 Scripts Overview

### 1. [`scripts/convert_and_index.py`](file:///home/roberto/Gits/cursosFC_UNAM/scripts/convert_and_index.py)
Converts PDF textbooks into Markdown (`./output/<book>.md`) and creates a local **LanceDB** vector database.
- **`--engine pymupdf` (`make index`)**: Fast CPU text extraction (~1s per book). Preserves text & plain Unicode formulas.
- **`--engine marker` (`make index-marker`)**: AI OCR layout parser (`marker_single`). Converts math layout into **true LaTeX equations (`$$...$$`)**.

**Execution:**
```bash
make index          # Fast text mode
make index-marker   # Full LaTeX math OCR mode
```

### 2. [`scripts/query_local.py`](file:///home/roberto/Gits/cursosFC_UNAM/scripts/query_local.py)
CLI tool to perform vector similarity queries against the local LanceDB index.

**Execution:**
```bash
make query
# OR
python3 scripts/query_local.py "Bose-Einstein condensation" --top_k 5
```

---

## 🐍 How to Extract Info Programmatically in Python

You can easily extract chunks, search results, or raw text directly in Python scripts or Jupyter/Colab notebooks:

```python
import lancedb
from sentence_transformers import SentenceTransformer

# 1. Connect to LanceDB index directory
db = lancedb.connect("./local_index/")
table = db.open_table("book_chunks")

# 2. Extract raw data into a Pandas DataFrame
df = table.to_pandas()
print(df[["source_id", "section", "text"]].head())

# 3. Perform a semantic vector query
model = SentenceTransformer("all-MiniLM-L6-v2")
query = "Equivalence of canonical and microcanonical ensembles"
query_vec = model.encode(query).tolist()

results = table.search(query_vec).limit(5).to_list()
for i, chunk in enumerate(results, start=1):
    print(f"Result #{i} | Book: {chunk['source_id']} | Section: {chunk['section']}")
    print(chunk["text"][:300])
    print("-" * 50)
```
