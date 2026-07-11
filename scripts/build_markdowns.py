# -*- coding: utf-8 -*-
import os
from site_livres_enfants_backend.livres_database import database
from site_livres_enfants_backend.config import root_directory
from site_livres_enfants_backend.livre import Livre, BooksCategory

os.chdir(root_directory)

MKDOCS_DIR_NAME = "site_livres_enfants_mkdocs"
DOCS_DIR_NAME = "docs"


def generate_category_page(
    title: str, 
    category_name: str, 
    books_category: BooksCategory,
    category_description: str, 
    livres: list[Livre],
) -> str:
    """Generate Markdown content for a category page."""
    lines = []
    lines.append("# " + title)
    lines.append("")
    lines.append("## Introduction")
    lines.append(category_description)
    lines.append("")

    for livre in livres:
        # category_content = getattr(livre, category_name, None)
        if books_category in livre.categories:
            lines.append("## " + livre.titre)
            if livre.couverture_path:
                lines.append("![Screenshot](img/" + livre.couverture_path + ")")
                lines.append("")
            lines.append(livre.description)
            lines.append("")

    return "\n".join(lines)


def write_category_markdown(
    filename: str, 
    title: str, 
    category_name: str, 
    category: BooksCategory, 
    category_description: str, 
    livres: list[Livre]
):
    """Generate and write a category Markdown file."""
    category_md = generate_category_page(
        title=title, 
        category_name=category_name, 
        books_category=category,
        category_description=category_description, 
        livres=livres
    )
    file_path = os.path.join(root_directory, MKDOCS_DIR_NAME, DOCS_DIR_NAME, filename)

    with open(file_path, mode="w", encoding="utf-8") as f:
        f.write(category_md)
    
    print("Generated: " + filename)


livres = database

write_category_markdown(
    filename="girls_empowerment.md",
    title="Girls empowerment",
    category_name="girl_empowerment",
    category=BooksCategory.GIRL_EMPOWERMENT,
    category_description="Des livres où des filles et des femmes jouent le premier role et sont inspirantes.",
    livres=livres,
)

write_category_markdown(
    filename="livres_sans_image.md",
    title="Livres sans images",
    category_name="livres_sans_image",
    category=BooksCategory.LIVRES_SANS_IMAGE,
    category_description="Des livres sans images, pour stimuler l'imagination.",
    livres=livres,
)