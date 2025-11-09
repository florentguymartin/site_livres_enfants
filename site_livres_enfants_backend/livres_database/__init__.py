from site_livres_enfants_backend.livre import Livre
from .by_prices import books_by_prices

database: list[Livre] = []

database += books_by_prices



