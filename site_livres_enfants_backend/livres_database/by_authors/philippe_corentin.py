from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

philippe_corentin_livres: list[Livre] = [
    Livre(
        titre="Plouf!",
        auteur=Author.PHILIPPE_CORENTIN,
        couverture_path="plouf.jpg",
        # todo: description needs to be entered manually afterwards
        description=(
            "to be filled"
        ),
        categories=(),
        age=(),
    ),
]
