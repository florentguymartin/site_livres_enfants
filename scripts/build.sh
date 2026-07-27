set -e # Exit immediately if a command exits with a non-zero status

# Build the markdown site which will be the starting point for MkDocs
python scripts/generate_and_write_markdowns.py

# Build the MkDocs site
# -s is strict mode: this will cause MkDocs to abort the build on any warnings.
# -c is clean: Remove old files from the site_dir before building
# -f  Provide a specific MkDocs config. This can be a file name.
mkdocs build -s -c -f site_livres_enfants_mkdocs/mkdocs.yml

# Serve the MkDocs site
# Run the builtin development server
# -o Open the website in a Web browser after the initial build finishes
# -f Provide a specific MkDocs config. This can be a file name, or '-' to read from stdin
mkdocs serve -o -f site_livres_enfants_mkdocs/mkdocs.yml