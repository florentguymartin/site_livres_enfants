from site_livres_enfants_backend.config import root_directory
from site_livres_enfants_backend.livre import Livre, BooksCategory, LivreRendererMarkdown
from site_livres_enfants_backend.livres_database.authors import Author, author_descriptions
import os

MKDOCS_DIR_NAME = "site_livres_enfants_mkdocs"
DOCS_DIR_NAME = "docs"


def generate_page(
    title: str, 
    introduction: str, 
    livres: list[Livre],
    img_folder: str | None = None,
) -> str:
    """Generate Markdown page with a list of books.

    Args:
        title (str): The title of the page.
        introduction (str): The introduction text for the page.
        livres (list[Livre]): The list of books to include on the page.
        img_folder (str | None): The folder containing book cover images.

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
        lines.append(livre_renderer.render_markdown(
            livre=livre,
            img_folder=img_folder
        ))
        lines.append("")

    return "\n".join(lines)


def _generate_category_page(
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
    books_category: BooksCategory, 
    books_category_description: str, 
    livres: list[Livre]
) -> None:
    """
    Generate and write a category Markdown file.
    
    Args:
        filename (str): The filename of the file to write.
        title (str): The title of the category.
        books_category (BooksCategory): The category of books.
        books_category_description (str): The description of the category.
        livres (list[Livre]): The list of books in the category.

    Returns:
        None
    """
    category_md = _generate_category_page(
        title=title, 
        books_category=books_category,
        category_description=books_category_description, 
        livres=livres
    )
    file_path = os.path.join(root_directory, MKDOCS_DIR_NAME, DOCS_DIR_NAME, filename)

    with open(file_path, mode="w", encoding="utf-8") as f:
        f.write(category_md)
    
    print("Generated: " + filename)





def generate_author_page(
    author: Author,
    author_description: str, 
    livres: list[Livre],
    title: str | None = None, 
    img_folder: str | None = None,
) -> str:
    """Generate Markdown content for an author page.
    Args:
        title (str | None): The title of the page.
        author (Author): The author of the books.
        author_description (str): The description of the author.
        livres (list[Livre]): The list of books by the author.

    Returns:
        The generated Markdown content as a string.
    """
    if title is None:
        title = author
    author_livres = [livre for livre in livres if livre.auteur == author]

    return generate_page(
        title=title,
        introduction=author_description,
        livres=author_livres,
        img_folder=img_folder,
    )

def to_snake_case(text):
    return text.strip().lower().replace(" ", "_")


def generate_author_pages(livres: list[Livre]) -> None:
    """Generate Markdown pages for all authors."""
    for author, description in author_descriptions.items():
        author_livres = [livre for livre in livres if livre.auteur == author]
        author_page = generate_author_page(
            author=author,
            author_description=description,
            livres=author_livres,
            img_folder="../img"
        )
        md_filename = to_snake_case(str(author))

        file_path_dir = os.path.join(root_directory, MKDOCS_DIR_NAME, DOCS_DIR_NAME, "authors")
        os.makedirs(file_path_dir, exist_ok=True)
        file_path = os.path.join(file_path_dir, md_filename + ".md")

        with open(file_path, mode="w", encoding="utf-8") as f:
            f.write(author_page)

        print("Generated: " + md_filename + ".md")

        # write_markdown_file(f"authors/{md_filename}.md", author_page)