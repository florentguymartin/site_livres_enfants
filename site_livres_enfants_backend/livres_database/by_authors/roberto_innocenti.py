from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

roberto_innocenti_livres: list[Livre] = [
    Livre(
        titre="La maison",
        auteur=Author.ROBERTO_INNOCENTI,
        couverture_path="la_maison.jpg",
        description="#todo",
    ),
]
