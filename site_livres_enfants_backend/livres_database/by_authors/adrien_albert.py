from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

adrien_albert_livres: list[Livre] = [
    Livre(
        titre="Un bisou pour mon frère",
        auteur=Author.ADRIEN_ALBERT,
        couverture_path="un_bisou_pour_mon_frere.jpg",
        # todo: description needs to be entered manually afterwards
        description=(
            "to be filled"
        ),
        categories=(),
        age=(),
    ),
]
