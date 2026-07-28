from site_livres_enfants_backend.livre import Livre
from site_livres_enfants_backend.livres_database.authors import Author

def is_author(livre: Livre, author: Author) -> bool:
    """Check if a book is written by a specific author."""
    if isinstance(livre.auteur, tuple):
        return author in livre.auteur
    else:
        return livre.auteur == author

def to_snake_case(text):
    return text.strip().lower().replace(" ", "_")

def sort_books_by_author_and_title(books: list[Livre]) -> list[Livre]:
    """Return a list of sorted books by author and title."""
    return sorted(books, key=lambda livre: (livre.get_author_as_str(), livre.titre))