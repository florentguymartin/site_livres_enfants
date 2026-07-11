from typing import List
from site_livres_enfants_backend.livre import Livre
from .by_prices import books_by_prices

database: List[Livre] = []

database += books_by_prices



