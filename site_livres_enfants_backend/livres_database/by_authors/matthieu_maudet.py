from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

matthieu_maudet_livres: list[Livre] = [
    Livre(
        titre="Occupé",
        auteur=Author.MATTHIEU_MAUDET,
        couverture_path="occupe.jpg",
        # todo: description needs to be entered manually afterwards
        description=(
            "to be filled"
        ),
        categories=(),
        age=(),
    ),
]
