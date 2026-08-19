.PHONY: index query setup clean-venv jupyter lab test-notebooks site-build site-dev help

VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip
JUPYTER = $(VENV)/bin/jupyter

setup:
	@echo "==> Creando entorno virtual Python en $(VENV)..."
	python3 -m venv $(VENV)
	@echo "==> Instalando dependencias desde requirements.txt..."
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	@if [ -f .env.example ] && [ ! -f .env ]; then cp .env.example .env; echo "==> Archivo .env inicializado."; fi
	@echo "==> ✅ Entorno configurado exitosamente. Para activarlo ejecuta: source $(VENV)/bin/activate"

clean-venv:
	@echo "==> Eliminando entorno virtual $(VENV)..."
	rm -rf $(VENV)
	@echo "==> Entorno virtual eliminado."

jupyter:
	@echo "==> Iniciando Jupyter Notebook en la carpeta Notebooks/..."
	$(JUPYTER) notebook --notebook-dir=Notebooks

lab:
	@echo "==> Iniciando Jupyter Lab..."
	$(JUPYTER) lab --notebook-dir=Notebooks

test-notebooks:
	@echo "==> Validando ejecución de notebooks de Python..."
	$(PYTHON) -c 'import json, glob, matplotlib; matplotlib.use("Agg"); [exec("".join(c["source"]), {}) for nb_file in glob.glob("Notebooks/Python/*.ipynb") for c in json.load(open(nb_file, encoding="utf-8"))["cells"] if c["cell_type"]=="code"]; print("✅ Todos los notebooks se ejecutaron sin errores.")'

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
	@echo "╔════════════════════════════════════════════════════════════════════╗"
	@echo "║       Comandos de Ayuda — Física Estadística (2027-1)              ║"
	@echo "╚════════════════════════════════════════════════════════════════════╝"
	@echo "  make setup          - Crea el entorno virtual .venv e instala dependencias"
	@echo "  make jupyter        - Inicia el servidor Jupyter Notebook local"
	@echo "  make lab            - Inicia el entorno Jupyter Lab local"
	@echo "  make test-notebooks - Ejecuta y valida todos los notebooks de Python"
	@echo "  make clean-venv     - Elimina el entorno virtual .venv"
	@echo "  make site-build     - Compila el sitio estático Quartz"
	@echo "  make site-dev       - Inicia servidor local de vista previa de Quartz"
	@echo "  make index          - Extracción e indexación rápida de PDFs (PyMuPDF)"
	@echo "  make index-marker   - Extracción con OCR LaTeX de PDFs (Marker)"
	@echo "  make query          - Realiza búsquedas en el índice RAG local"
