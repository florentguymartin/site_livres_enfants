from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

claude_boujon_livres: list[Livre] = [
    Livre(
        titre="La brouille",
        auteur=Author.CLAUDE_BOUJON,
        couverture_path="la_brouille.jpg",
        description="#todo",
    ),
    Livre(
        titre="La chaise bleue",
        auteur=Author.CLAUDE_BOUJON,
        couverture_path="la_chaise_bleue.jpg",
        description="#todo",
    ),
]
