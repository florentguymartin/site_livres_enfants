from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

josse_goffin_livres: list[Livre] = [
    Livre(
        titre="Oh",
        auteur=Author.JOSSE_GOFFIN,
        couverture_path="oh.jpg",
        description=(
            "to be filled"
        ),
        categories=(),
        age=()
        #todo: description needs to be entered manually afterwards
    ),
]
