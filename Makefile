.PHONY: index query setup site-build site-dev help

VENV = .venv
PYTHON = $(VENV)/bin/python

setup:
	python3 -m venv $(VENV)
	$(VENV)/bin/pip install -r requirements.txt
	cp .env.example .env || true
	@echo "Now edit .env with your PDF_DIR"

index:
	$(PYTHON) scripts/convert_and_index.py --engine pymupdf

index-marker:
	$(PYTHON) scripts/convert_and_index.py --engine marker

query:
	@read -p "Enter query: " q; \
	$(PYTHON) scripts/query_local.py "$$q"

site-build:
	npx quartz build -d .

site-dev:
	npx quartz build --serve -d .

help:
	@echo "make setup         - create venv and install deps"
	@echo "make index         - fast text extraction (PyMuPDF)"
	@echo "make index-marker  - full LaTeX math OCR extraction (Marker)"
	@echo "make query         - search the local index"
	@echo "make site-build    - build static site locally"
	@echo "make site-dev      - preview site on localhost"
