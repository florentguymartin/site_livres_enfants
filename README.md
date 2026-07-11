# Livres pour Enfants – Static Website Generator

A Python-based static site generator for curating and showcasing children's books with categorization by theme, author, and price range.

## Essential Dev
put cover images in 'site_livres_enfants_mkdocs/docs/img'


## 📦 Installation

### Prerequisites
- Conda (Anaconda or Miniconda)

### Setup Instructions

1. **Create a Conda environment:**
   ```bash
   conda create -n env_site_livres python=3.11
   conda activate env_site_livres
   ```

2. **Install the project in editable mode:**
   ```bash
   pip install -e .
   ```

This will install the `site_livres_enfants_backend` package and all dependencies specified in `pyproject.toml`.

## 🎯 Project Overview

This project generates a static website featuring children's literature recommendations. It combines:
- **Pydantic-based data models** for type-safe book metadata
- **Python string building** to dynamically generate Markdown pages from book data
- **MkDocs + Material theme** to build and serve the static site

The workflow follows a classic **data-driven site generation pattern**: Python code defines the book database, Python functions build that data into Markdown files, and MkDocs builds the final HTML.

## 📁 Project Structure

```
site_livres_enfants/
├── site_livres_enfants_backend/          # Core Python package
│   ├── config.py                         # Project configuration (root directory)
│   ├── livre.py                          # Livre (Book) Pydantic model
│   └── livres_database/
│       ├── __init__.py                   # Aggregates all book sources
│       └── by_prices/
│           ├── __init__.py
│           └── medaille_caldecott.py     # Book data (e.g., Caldecott award winners)
│
├── site_livres_enfants_mkdocs/           # MkDocs configuration & output
│   ├── mkdocs.yml                        # Site structure & theme settings
│   ├── docs/                             # Source Markdown files
│   │   ├── index.md                      # Homepage
│   │   ├── par_auteurs.md                # Books by author
│   │   ├── girls_empowerment.md          # (Generated dynamically)
│   │   └── img/                          # Book cover images
│   └── site/                             # Built HTML output
│
├── scripts/
│   ├── build_markdowns.py                # Generates Markdown from Python data
│   └── build.sh                          # Build & serve workflow
│
├── pyproject.toml                        # Project metadata & dependencies
└── README.md                             # This file
```

## 🔧 Key Components

### 1. **Data Model: `Livre` (Book)**
Defined in `site_livres_enfants_backend/livre.py`:
```python
class Livre(BaseModel):
    titre: str                          # Book title
    auteur: str                         # Author name
    couverture_path: str | None = None  # Cover image path
    girl_empowerment: str | None = None # Thematic metadata for filtering
```
Uses Pydantic for validation and serialization.

### 2. **Book Database**
- Located in `site_livres_enfants_backend/livres_database/`
- Organized by categories: `by_prices/`, `by_authors/` (extensible)
- Each module (e.g., `medaille_caldecott.py`) defines book instances
- All books are aggregated in `__init__.py`

### 3. **Markdown Generation: Pure Python**
`scripts/build_markdowns.py` generates Markdown files directly:
- `generate_category_page()` builds Markdown content from book data
- Loops through books filtered by category (e.g., `girl_empowerment`)
- Renders book titles, descriptions, and cover images as strings
- Output is written to `site_livres_enfants_mkdocs/docs/`

### 4. **Static Site Builder: MkDocs**
- Configured in `site_livres_enfants_mkdocs/mkdocs.yml`
- Uses Material theme for responsive design
- Reads generated Markdown and outputs static HTML to `site/`

## 🚀 How It Works

### Build Pipeline

```
┌─────────────────────────────────────────────┐
│ Python Book Database (Pydantic models)      │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────┐
│ Python String Building                      │
│ (build_markdowns.py)                        │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────┐
│ Generated Markdown Files                    │
│ (docs/girls_empowerment.md, etc.)           │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────┐
│ MkDocs Build                                │
│ (mkdocs build)                              │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────┐
│ Static HTML Website                         │
│ (site_livres_enfants_mkdocs/site/)          │
└─────────────────────────────────────────────┘
```

## 🛠️ Getting Started

### Prerequisites
- Python ≥ 3.13
- Dependencies: `mkdocs`, `pydantic`, `mkdocs-material` (see `pyproject.toml`)

### Installation
```bash
pip install -e .
```

### Build & Serve

```bash
bash scripts/build.sh
```

This script:
1. Runs `scripts/build_markdowns.py` → Generates Markdown from Python data
2. Runs `mkdocs build` → Builds static HTML
3. Runs `mkdocs serve` → Serves the site locally (opens in browser)

### Manual Steps
```bash
# Generate Markdown from Python data
python scripts/build_markdowns.py

# Build static site
mkdocs build -s -c -f site_livres_enfants_mkdocs/mkdocs.yml

# Serve locally
mkdocs serve -o -f site_livres_enfants_mkdocs/mkdocs.yml
```

## 📚 Adding Books

1. **Create or edit a book source file** (e.g., `site_livres_enfants_backend/livres_database/by_prices/medaille_caldecott.py`)
2. **Instantiate `Livre` objects** with metadata:
   ```python
   from site_livres_enfants_backend.livre import Livre
   
   my_book = Livre(
       titre="Mon Livre",
       auteur="Auteur Français",
       girl_empowerment="Description of why this book empowers girls...",
       couverture_path="mon_livre.jpg",
   )
   ```
3. **Add to the database** list in the module
4. **Export** from `livres_database/__init__.py`:
   ```python
   from .by_prices import books_by_prices
   database: list[Livre] = []
   database += books_by_prices
   ```
5. **Rebuild** with `bash scripts/build.sh`

## 🎨 Customization

### Add a New Category Page
1. Add new field to `Livre` model in `site_livres_enfants_backend/livre.py` (e.g., `adventure: Optional[str] = None`)
2. Add book metadata to your data source (e.g., `medaille_caldecott.py`)
3. Add a new generation call in `scripts/build_markdowns.py`:
   ```python
   write_category_markdown(
       filename="adventure.md",
       title="Adventure Stories",
       category_name="adventure",
       category_description="Books about exploration and adventure...",
       livres=livres,
   )
   ```
4. Update `mkdocs.yml` to include the new page in navigation
5. Run `bash scripts/build.sh` to regenerate

## 📦 Dependencies

| Package | Purpose |
|---------|---------|
| `pydantic` | Type-safe data models & validation |
| `mkdocs` | Static site generator |
| `mkdocs-material` | Professional Material design theme |

## 📝 License

MIT (see `pyproject.toml`)

## 👨‍💻 Author

Florent Martin – florent.guy.martin@gmail.com
