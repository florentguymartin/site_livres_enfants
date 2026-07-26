from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

haruo_yamashita_livres: list[Livre] = [
    Livre(
        titre="Les souris à la plage",
        auteur=Author.HARUO_YAMASHITA,
        couverture_path="les_souris_a_la_plage.jpg",
        # todo: description needs to be entered manually afterwards
        description=(
            "to be filled"
        ),
        categories=(),
        age=(),
    ),
]
