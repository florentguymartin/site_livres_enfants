from typing import List
from site_livres_enfants_backend.livre import Livre
from .by_prices import books_by_prices
from .by_authors.by_authors import by_authors_books

database: List[Livre] = []

database += books_by_prices
database += by_authors_books
