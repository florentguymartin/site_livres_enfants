from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

jean_claverie_livres: list[Livre] = [
    Livre(
        titre="L'art du pot",
        auteur=(Author.JEAN_CLAVERIE, Author.MICHELE_NIKLY),
        couverture_path="l_art_du_pot.jpg",
        description="#todo",
    ),
]
