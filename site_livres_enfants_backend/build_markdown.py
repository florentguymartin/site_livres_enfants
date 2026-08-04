"""Module with functions to generate Markdown files for the site."""


from site_livres_enfants_backend.config import root_directory
from site_livres_enfants_backend.livre import (
    Livre, BooksCategory, LivreRendererMarkdown, category_descriptions, age_descriptions, BooksAge
)
from site_livres_enfants_backend.livres_database.authors import Author, author_descriptions
from site_livres_enfants_backend.backend_utils import is_author, to_snake_case, sort_books_by_author_and_title
from site_livres_enfants_backend.book_awards import BookAward, GenericBookAward, award_descriptions
import os

MKDOCS_DIR_NAME = "site_livres_enfants_mkdocs"
DOCS_DIR_NAME = "docs"


TOP_TEN_BOOK_TITLES = (
    "Flotman",
    "Juliette et Bellini",
    "La famille souris dîne au clair de lune",
    "Grosse Légume",
    "La visite",
    "Boréal-Express",
    "Une histoire à quatre voix",
    "Vert secret",
    "Avant Après",
    "L'album d'Adèle",
)

TOP_TEN_TITLE = "Choisir c'est renoncer"
TOP_TEN_INTRODUCTION = (
    "Choisir c'est renoncer. Voici donc 10 livres qui pourraient former un top 10, "
    "présentés dans l'ordre défini dans le README."
)

def make_page_md(
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
    if not isinstance(introduction, str):
        raise ValueError(f"Introduction must be a string but got {introduction} with type {type(introduction).__name__}")

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


def _make_category_page_md(
    title: str, 
    books_category: BooksCategory,
    category_description: str, 
    livres: list[Livre],
    img_folder: str | None = None
) -> str:
    """Generate Markdown content for a category page.
    Args:
        title (str): The title of the page.
        books_category (BooksCategory): The category of books.
        category_description (str): The description of the category.
        livres (list[Livre]): The list of books in the category.
        img_folder (str | None): The folder containing book cover images.

    Returns:
        The generated Markdown content as a string.
    """
    category_livres = [livre for livre in livres if books_category in livre.categories]

    return make_page_md(
        title=title,
        introduction=category_description,
        livres=category_livres,
        img_folder=img_folder
    )

def _make_age_page_md(
    title: str, 
    books_age: BooksAge,
    age_description: str, 
    livres: list[Livre],
    img_folder: str | None = None
) -> str:
    """Generate Markdown content for an age page.
    Args:
        title (str): The title of the page.
        books_age (BooksAge): The age group of books.
        age_description (str): The description of the age group.
        livres (list[Livre]): The list of books in the age group.
        img_folder (str | None): The folder containing book cover images.

    Returns:
        The generated Markdown content as a string.
    """
    age_livres = [livre for livre in livres if books_age in livre.age]

    return make_page_md(
        title=title,
        introduction=age_description,
        livres=age_livres,
        img_folder=img_folder
    )


def _make_author_page_md(
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
    author_livres = [livre for livre in livres if is_author(livre, author)]

    return make_page_md(
        title=title,
        introduction=author_description,
        livres=author_livres,
        img_folder=img_folder,
    )

def write_age_page_md(
    filename: str, 
    title: str, 
    books_age: BooksAge, 
    age_description: str, 
    livres: list[Livre]
) -> None:
    """
    Generate and write an age Markdown file.
    Args:
        filename (str): The filename of the file to write. Must include the .md extension
        title (str): The title of the age group.
        books_age (BooksAge): The age group of books.
        age_description (str): The description of the age group.
        livres (list[Livre]): The list of books in the age group.

    Returns:
        None
    """
    if not filename.endswith(".md"):
        raise ValueError(f"Filename must end with .md extension: {filename}")

    sorted_books = sort_books_by_author_and_title(livres)

    age_md = _make_age_page_md(
        title=title, 
        books_age=books_age,
        age_description=age_description, 
        livres=sorted_books,
        img_folder="../img",
    )

    file_path_dir = os.path.join(root_directory, MKDOCS_DIR_NAME, DOCS_DIR_NAME, "age")
    os.makedirs(file_path_dir, exist_ok=True)
    file_path = os.path.join(file_path_dir, filename)

    with open(file_path, mode="w", encoding="utf-8") as f:
        f.write(age_md)

    print("Generated: " + filename)

def write_category_page_md(
    filename: str, 
    title: str, 
    books_category: BooksCategory, 
    books_category_description: str, 
    livres: list[Livre]
) -> None:
    """
    Generate and write a category Markdown file.
    Args:
        filename (str): The filename of the file to write. Must include the .md extension
        title (str): The title of the category.
        books_category (BooksCategory): The category of books.
        books_category_description (str): The description of the category.
        livres (list[Livre]): The list of books in the category.

    Returns:
        None
    """
    if not filename.endswith(".md"):
        raise ValueError(f"Filename must end with .md extension: {filename}")

    sorted_books = sort_books_by_author_and_title(livres)

    category_md = _make_category_page_md(
        title=title, 
        books_category=books_category,
        category_description=books_category_description, 
        livres=sorted_books,
        img_folder="../img"
    )
    file_path_dir = os.path.join(root_directory, MKDOCS_DIR_NAME, DOCS_DIR_NAME, "categories")
    os.makedirs(file_path_dir, exist_ok=True)
    file_path = os.path.join(file_path_dir, filename)

    with open(file_path, mode="w", encoding="utf-8") as f:
        f.write(category_md)
    
    print("Generated: " + filename)


def write_author_page_md(
    filename: str, 
    title: str, 
    author: Author, 
    author_description: str, 
    livres: list[Livre]
) -> None:
    """
    Generate and write an author Markdown file.

    Args:
        filename (str): The filename of the file to write. Must include the .md extension
        title (str): The title of the author.
        author (Author): The author of the books.
        author_description (str): The description of the author.
        livres (list[Livre]): The list of books by the author.

    Returns:
        None
    """
    if not filename.endswith(".md"):
        raise ValueError(f"Filename must end with .md extension: {filename}")

    sorted_books = sort_books_by_author_and_title(livres)

    author_md = _make_author_page_md(
        author=author,
        author_description=author_description,
        livres=sorted_books, 
        img_folder="../img",
    )

    md_filename = to_snake_case(str(author)) + ".md"
    file_path_dir = os.path.join(root_directory, MKDOCS_DIR_NAME, DOCS_DIR_NAME, "authors")
    os.makedirs(file_path_dir, exist_ok=True)
    file_path = os.path.join(file_path_dir, md_filename)


    with open(file_path, mode="w", encoding="utf-8") as f:
        f.write(author_md)

    print("Generated: " + md_filename)


def write_all_category_pages_md(
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
    for books_category, (title, description) in category_descriptions.items():
        write_category_page_md(
            filename=books_category.value + ".md",
            title=title,
            books_category=books_category,
            books_category_description=description,
            livres=livres
        )

def write_all_age_pages_md(
    livres: list[Livre]
) -> None:
    """
    Generate and write age Markdown files for all age groups.
    Args:
        livres (list[Livre]): The list of books to categorize by age group.

    Returns:
        None
    """
    for books_age, (title, description) in age_descriptions.items():
        write_age_page_md(
            filename=books_age.value + ".md",
            title=title,
            books_age=books_age,
            age_description=description,
            livres=livres
        )

def write_all_author_pages(livres: list[Livre]) -> None:
    """Generate and write Markdown pages for all authors."""
    for author, description in author_descriptions.items():
        author_livres = [livre for livre in livres if livre.auteur == author]
        write_author_page_md(
            filename=to_snake_case(str(author)) + ".md",
            title=str(author),
            author=author,
            author_description=description,
            livres=author_livres
        )


def _has_award(livre: Livre, award_class: type[GenericBookAward]) -> bool:
    """Check if a book has a specific award type."""
    if livre.awards is None:
        return False
    if isinstance(livre.awards, BookAward):
        return isinstance(livre.awards, award_class)
    return any(isinstance(award, award_class) for award in livre.awards)


def _make_book_award_page_md(
    title: str,
    award_class: type[GenericBookAward],
    award_description: str,
    livres: list[Livre],
    img_folder: str | None = None,
) -> str:
    """Generate Markdown content for a book award page.

    Args:
        title (str): The title of the page.
        award_class (type[GenericBookAward]): The book award class to filter by.
        award_description (str): The description of the award.
        livres (list[Livre]): The list of books to filter.
        img_folder (str | None): The folder containing book cover images.

    Returns:
        The generated Markdown content as a string.
    """
    award_livres = [livre for livre in livres if _has_award(livre, award_class)]

    return make_page_md(
        title=title,
        introduction=award_description,
        livres=award_livres,
        img_folder=img_folder,
    )


def write_book_award_page_md(
    filename: str,
    title: str,
    award_class: type[GenericBookAward],
    award_description: str,
    livres: list[Livre],
) -> None:
    """Generate and write a book award Markdown file.

    Args:
        filename (str): The filename of the file to write. Must include the .md extension.
        title (str): The title of the award page.
        award_class (type[GenericBookAward]): The book award class to filter by.
        award_description (str): The description of the award.
        livres (list[Livre]): The list of books to filter.

    Returns:
        None
    """
    if not filename.endswith(".md"):
        raise ValueError(f"Filename must end with .md extension: {filename}")

    sorted_books = sort_books_by_author_and_title(livres)

    award_md = _make_book_award_page_md(
        title=title,
        award_class=award_class,
        award_description=award_description,
        livres=sorted_books,
        img_folder="../img",
    )

    file_path_dir = os.path.join(root_directory, MKDOCS_DIR_NAME, DOCS_DIR_NAME, "book_awards")
    os.makedirs(file_path_dir, exist_ok=True)
    file_path = os.path.join(file_path_dir, filename)

    with open(file_path, mode="w", encoding="utf-8") as f:
        f.write(award_md)

    print("Generated: " + filename)


def write_top_ten_page_md(livres: list[Livre]) -> None:
    """Generate and write the top 10 Markdown file."""
    books_by_title = {livre.titre: livre for livre in livres}
    missing_titles = [title for title in TOP_TEN_BOOK_TITLES if title not in books_by_title]
    if missing_titles:
        raise ValueError(f"Top 10 books not found in database: {', '.join(missing_titles)}")

    top_ten_books = [books_by_title[title] for title in TOP_TEN_BOOK_TITLES]
    top_ten_md = make_page_md(
        title=TOP_TEN_TITLE,
        introduction=TOP_TEN_INTRODUCTION,
        livres=top_ten_books,
        img_folder="../img",
    )

    file_path_dir = os.path.join(root_directory, MKDOCS_DIR_NAME, DOCS_DIR_NAME, "introduction")
    os.makedirs(file_path_dir, exist_ok=True)
    file_path = os.path.join(file_path_dir, "choisir.md")

    with open(file_path, mode="w", encoding="utf-8") as f:
        f.write(top_ten_md)

    print("Generated: choisir.md")


def write_all_book_award_pages_md(livres: list[Livre]) -> None:
    """Generate and write Markdown pages for all book awards.

    Args:
        livres (list[Livre]): The list of books to categorize by award.

    Returns:
        None
    """
    for award_class, (title, description, filename_stem) in award_descriptions.items():
        filename = filename_stem + ".md"
        write_book_award_page_md(
            filename=filename,
            title=title,
            award_class=award_class,
            award_description=description,
            livres=livres,
        )