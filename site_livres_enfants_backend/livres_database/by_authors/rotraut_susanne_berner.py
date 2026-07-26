from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

rotraut_susanne_berner_livres: list[Livre] = [
    Livre(
        titre="Le livre de l'été",
        auteur=Author.ROTRAUT_SUSANNE_BERNER,
        couverture_path="sommer_wimmelbuch.jpg",
        # todo: description needs to be entered manually afterwards
        description=(
            "to be filled"
        ),
        categories=(),
        age=(),
    ),
]
