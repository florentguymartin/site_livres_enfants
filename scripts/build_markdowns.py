from dataclasses import dataclass
import os
import jinja2
from site_livres_enfants_backend.livres_database import database
from site_livres_enfants_backend.config import root_directory

os.chdir(root_directory)

MKDOCS_DIR_NAME = "site_livres_enfants_mkdocs"
DOCS_DIR_NAME = "docs"

GIRL_EMPOWERMENT_MD_FILENAME = "girls_empowerment.md"

environment = jinja2.Environment(loader=jinja2.FileSystemLoader("jinja_templates"))
template = environment.get_template("template_page_categorie_livres.md.jinja")

livres = database

category_name = "girl_empowerment"
title = "Girls empowerment"
category_description = """Des livres où des filles et des femmes jouent le premier role et sont inspirantes."""

category_md = template.render(
    title=title,
    category_name=category_name,
    category_description=category_description,
    livres=livres,
)

file_path = os.path.join(root_directory, MKDOCS_DIR_NAME, DOCS_DIR_NAME, GIRL_EMPOWERMENT_MD_FILENAME)
with open(file_path, mode="w", encoding="utf-8") as f:
    f.write(category_md)
