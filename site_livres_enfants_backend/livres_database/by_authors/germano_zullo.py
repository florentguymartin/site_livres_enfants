from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

germano_zullo_livres: list[Livre] = [
    Livre(
        titre="La Rumeur de Venise",
        auteur=(Author.ALBERTINE, Author.GERMANO_ZULLO),
        couverture_path="la_rumeur_de_venise.jpg",
        description="#todo",
    ),
]
