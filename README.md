# 📚 Master Course Template — cursosFC_UNAM

A version-controlled, Obsidian-compatible master course template and learning system for physics courses at **Facultad de Ciencias, UNAM**, created and maintained by **Dr. Roberto Antonio Zamora Zamora**.

---

## 🌟 Overview & Architecture

This repository serves as the **Master Template (`main` branch)** for generating isolated, interactive, and version-controlled websites for university courses (such as *Física Estadística*, *Matemáticas Avanzadas para la Física*, *Dinámica de Medios Deformables*, etc.).

It integrates three foundational pillars:

1. **Obsidian Knowledge Vault (Public & Git-Tracked)**:
   - Atomic concept notes (`Concepts/`), lecture logs (`Lectures/`), Map of Content portals (`MoC/`), evaluation guidelines (`Projects/`), and syllabus definitions (`Syllabus.md`).
   - Rich Markdown frontmatter, LaTeX equation rendering (`$$...$$`), and Obsidian wikilinks (`[[Concept]]`).

2. **Public Static Web Interface via Quartz 5 (Automated Web Deployment)**:
   - Publishes the interactive vault to **GitHub Pages** without requiring students to install Obsidian or Git.
   - Includes full-text search, visual graph view, backlinks, popover previews, and KaTeX rendering.

3. **Private PDF Indexing RAG Pipeline (Local & Private)**:
   - Python tools (`scripts/convert_and_index.py`, `scripts/query_local.py`) to convert textbook PDFs into searchable vector chunks via **LanceDB** for deep offline semantic retrieval without committing copyrighted PDFs.

---

## 🌿 Git Branching Strategy (Per Semester / Course)

To maintain a clean master template while running active courses, use **Git Branching per Term**:

```bash
# 1. Clone the master repository
git clone https://github.com/razamoraz/cursosFC_UNAM.git
cd cursosFC_UNAM

# 2. Create a dedicated branch for a new semester term (e.g. 2026-1 Física Estadística)
git checkout -b 2026-1-fisica-estadistica

# 3. Customize Syllabus.md, schedule dates, and publish to GitHub Pages
git add .
git commit -m "feat: initialize 2026-1 course instance for Física Estadística"
```

*Note:* Standard template updates or core script fixes made in active branches can be cleanly merged back into `main`.

---

## 📁 Repository Structure

```
.
├── Syllabus.md                         # Official Course Syllabus (Temario, Evaluation 50/40/10, AI Policy)
├── index.md                            # Quartz static site homepage
├── Concepts/                           # Atomic concept notes by domain
│   ├── Ensembles/
│   ├── Thermodynamics/
│   ├── Quantum_Statistics/
│   ├── Kinetic_Theory_Numerics/
│   ├── Phase_Transitions/
│   └── Mathematical_Tools/
├── Notebooks/                          # Google Colab notebooks for numerical methods
│   ├── Python/                         # Jupyter notebooks (NumPy, SciPy, PyCUDA, JAX)
│   └── Julia/                          # High-performance Julia notebooks
├── Projects/                           # Final project guidelines & paper proposal templates
│   ├── Final_Project_Guide.md          # 40% Final Project Guide (7-15 min video + oral defense)
│   └── Paper_Proposal_Template.md      # Week 8-9 Paper Selection proposal template
├── MoC/                                # Maps of Content (Entry portals by block)
│   └── Statistical_Physics_MoC.md
├── Lectures/                           # Chronological course materials & lecture notes
│   └── Week_01_Introduction.md
├── Sources/                            # Metadata for textbooks and papers
├── Source_Registers/                   # Concept-to-literature mappings
├── Templates/                          # Obsidian note & syllabus templates
│   ├── Concept.md
│   ├── Lecture.md
│   ├── Syllabus_Template.md
│   └── Project_Rubric.md
├── scripts/                            # Local Python RAG indexing & CLI query tools
│   ├── convert_and_index.py
│   └── query_local.py
├── .github/workflows/
│   ├── validate.yml                    # CI vault validation
│   └── deploy.yml                      # Quartz GitHub Pages deployment
├── quartz.config.yaml                  # Quartz configuration file
├── Makefile                            # Development & deployment shortcuts
└── README.md
```

---

## 🚀 Getting Started

### 1. Local Web Preview (Quartz)
Ensure Node.js 22+ is installed, then run:

```bash
# Install Node dependencies
npm install

# Preview site locally on http://localhost:8080
make site-dev

# Build static HTML production bundle into public/
make site-build
```

### 2. Private PDF RAG & Markdown Pipeline (Optional)
Convert local textbook PDFs into Markdown (`./output/<book>.md`) and build an offline LanceDB vector index:

```bash
# 1. Initialize Python environment & dependencies
make setup

# 2. Place PDFs in ./sample_pdfs/ (or set PDF_DIR in .env)

# 3a. Fast text mode (PyMuPDF - plain text formulas)
make index

# 3b. Full LaTeX math OCR mode (Marker - genuine $$...$$ equations)
make index-marker

# 4. Search local vector index
make query
```
*Note:* Converted Markdown files are saved locally to `./output/*.md` for easy copy-pasting of LaTeX equations and AI prompting. All PDFs and output files are `.gitignore`d for copyright safety.

---

## 💯 Course Evaluation Framework (Física Estadística)

- **50% Monthly Exams**: Lowest score dropped. **+1 bonus point per exam** when handing in a 1-page handwritten formula/cheat sheet.
- **40% Final Project**: Discussion or numerical reproduction of a published scientific paper (individual or max 3).
  - **Week 8–9**: Paper proposal submission (1 page).
  - **End of Term**: 7–15 min video presentation + 15 min oral defense.
- **10% Feedback**: Participation (>90%) in weekly Google Forms feedback.
- **AI Policy**: AI tools (LLMs) are permitted for code/writing assistance if prompt logs are explicitly disclosed. Strictly forbidden during exams and oral defenses.

---

## 🌐 GitHub Pages Deployment

The included GitHub Actions workflow (`.github/workflows/deploy.yml`) automatically builds and deploys Quartz whenever changes are pushed to `main` or active course branches.

Set **Settings > Pages > Source** to `GitHub Actions` in your GitHub repository settings.
