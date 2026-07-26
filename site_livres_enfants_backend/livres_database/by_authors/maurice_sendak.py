from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

maurice_sendak_livres: list[Livre] = [
    Livre(
        titre="Max et les Maximonstres",
        auteur=Author.MAURICE_SENDAK,
        couverture_path="max_et_les_maximonstres.jpg",
        # todo: description needs to be entered manually afterwards
        description=(
            "to be filled"
        ),
        categories=(),
        age=(),
    ),
]
