# -*- coding: utf-8 -*-
import os
from site_livres_enfants_backend.livres_database import database
from site_livres_enfants_backend.config import root_directory

os.chdir(root_directory)

MKDOCS_DIR_NAME = "site_livres_enfants_mkdocs"
DOCS_DIR_NAME = "docs"


def generate_category_page(title, category_name, category_description, livres):
    """Generate Markdown content for a category page."""
    lines = []
    lines.append("# " + title)
    lines.append("")
    lines.append("## Introduction")
    lines.append(category_description)
    lines.append("")

    for livre in livres:
        category_content = getattr(livre, category_name, None)
        if category_content:
            lines.append("## " + livre.titre)
            if livre.couverture_path:
                lines.append("![Screenshot](img/" + livre.couverture_path + ")")
                lines.append("")
            lines.append(category_content)
            lines.append("")

    return "\n".join(lines)


def write_category_markdown(filename, title, category_name, category_description, livres):
    """Generate and write a category Markdown file."""
    category_md = generate_category_page(title, category_name, category_description, livres)
    file_path = os.path.join(root_directory, MKDOCS_DIR_NAME, DOCS_DIR_NAME, filename)
    
    with open(file_path, mode="w", encoding="utf-8") as f:
        f.write(category_md)
    
    print("Generated: " + filename)


livres = database

write_category_markdown(
    "girls_empowerment.md",
    "Girls empowerment",
    "girl_empowerment",
    "Des livres où des filles et des femmes jouent le premier role et sont inspirantes.",
    livres,
)
