from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

anais_vaugelade_livres: list[Livre] = [
    Livre(
        titre="Le secret",
        auteur=Author.ANAIS_VAUGELADE,
        couverture_path="le_secret.jpg",
        # todo: description needs to be entered manually afterwards
        description=(
            "to be filled"
        ),
        categories=(),
        age=(),
    ),
]
