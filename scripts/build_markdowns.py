# -*- coding: utf-8 -*-
import os
from site_livres_enfants_backend.livres_database import database
from site_livres_enfants_backend.config import root_directory
from site_livres_enfants_backend.livre import Livre, BooksCategory, LivreRendererMarkdown

os.chdir(root_directory)

MKDOCS_DIR_NAME = "site_livres_enfants_mkdocs"
DOCS_DIR_NAME = "docs"


def generate_page(
    title: str, 
    introduction: str, 
    livres: list[Livre],
) -> str:
    """Generate Markdown page content for a category page.

    Args:
        title (str): The title of the page.
        introduction (str): The introduction text for the page.
        livres (list[Livre]): The list of books to include on the page.
    
    Returns:
        The generated Markdown content as a string.
    """
    lines = []
    lines.append("# " + title)
    lines.append("")
    lines.append("## Introduction")
    lines.append(introduction)
    lines.append("")

    livre_renderer = LivreRendererMarkdown()

    for livre in livres:
        lines.append(livre_renderer.render_markdown(livre))
        lines.append("")

    return "\n".join(lines)


def generate_category_page(
    title: str, 
    books_category: BooksCategory,
    category_description: str, 
    livres: list[Livre],
) -> str:
    """Generate Markdown content for a category page.
    Args:
        title (str): The title of the page.
        books_category (BooksCategory): The category of books.
        category_description (str): The description of the category.
        livres (list[Livre]): The list of books in the category.
    
    Returns:
        The generated Markdown content as a string.
    """
    category_livres = [livre for livre in livres if books_category in livre.categories]

    return generate_page(
        title=title,
        introduction=category_description,
        livres=category_livres
    )


def write_category_markdown(
    filename: str, 
    title: str, 
    category: BooksCategory, 
    category_description: str, 
    livres: list[Livre]
) -> None:
    """
    Generate and write a category Markdown file.
    
    Args:
        filename (str): The name of the file to write.
        title (str): The title of the category.
        category (BooksCategory): The category of books.
        category_description (str): The description of the category.
        livres (list[Livre]): The list of books in the category.

    Returns:
        None
    """
    category_md = generate_category_page(
        title=title, 
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
    category=BooksCategory.GIRL_EMPOWERMENT,
    category_description="Des livres où des filles et des femmes jouent le premier role et sont inspirantes.",
    livres=livres,
)

write_category_markdown(
    filename="livres_sans_image.md",
    title="Livres sans images",
    category=BooksCategory.LIVRES_SANS_IMAGE,
    category_description="Des livres sans images, pour stimuler l'imagination.",
    livres=livres,
)