from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

suzy_lee_livres: list[Livre] = [
    Livre(
        titre="La Vague",
        auteur=Author.SUZY_LEE,
        couverture_path="la_vague.jpg",
        # todo: description needs to be entered manually afterwards
        description=(
            "to be filled"
        ),
        categories=(),
        age=(),
    ),
]
