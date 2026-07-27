from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

junko_nakamura_livres: list[Livre] = [
    Livre(
        titre="La visite",
        auteur=Author.JUNKO_NAKAMURA,
        couverture_path="la_visite.jpg",
        # todo: description needs to be entered manually afterwards
        description=(
            "to be filled"
        ),
        categories=(),
        age=(),
    ),
]
