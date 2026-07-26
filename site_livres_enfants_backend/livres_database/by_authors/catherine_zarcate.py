from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

catherine_zarcate_livres: list[Livre] = [
    Livre(
        titre="Les poulets guerriers",
        auteur=Author.CATHERINE_ZARCATE,
        couverture_path="les_poulets_guerriers.jpg",
        # todo: description needs to be entered manually afterwards
        description=(
            "to be filled"
        ),
        categories=(),
        age=(),
    ),
]
