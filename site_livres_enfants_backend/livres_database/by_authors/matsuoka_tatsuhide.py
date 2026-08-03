from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

matsuoka_tatsuhide_livres: list[Livre] = [
    Livre(
        titre="Saute",
        auteur=Author.MATSUOKA_TATSUHIDE,
        couverture_path="saute.jpg",
        description=(
            "to be filled"
        ),
        categories=(),
        age=()
        #todo: description needs to be entered manually afterwards
    ),
]
