from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

germano_zullo_livres: list[Livre] = [
    Livre(
        titre="Ligne 135",
        auteur=Author.GERMANO_ZULLO,
        couverture_path="ligne_135.jpg",
        # todo: description needs to be entered manually afterwards
        description=(
            "to be filled"
        ),
        categories=(),
        age=(),
    ),
]
