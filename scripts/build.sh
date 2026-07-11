set -e
python scripts/build_markdowns.py
# cd site_livres_enfants_backend

mkdocs build -s -c -f site_livres_enfants_mkdocs/mkdocs.yml
mkdocs serve -o -f site_livres_enfants_mkdocs/mkdocs.yml