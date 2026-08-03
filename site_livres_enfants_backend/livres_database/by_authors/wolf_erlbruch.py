from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

wolf_erlbruch_livres: list[Livre] = [
    Livre(
        titre="La grande question",
        auteur=Author.WOLF_ERLBRUCH,
        couverture_path="la_grande_question.jpg",
        description=(
            "to be filled"
        ),
        categories=(),
        age=()
        #todo: description needs to be entered manually afterwards
    ),
]
