from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

martin_waddell_livres: list[Livre] = [
    Livre(
        titre="Tu ne dors pas, petit ours?",
        auteur=Author.MARTIN_WADDELL,
        couverture_path="tu_ne_dors_pas_petit_ours.jpg",
        # todo: description needs to be entered manually afterwards
        description=(
            "to be filled"
        ),
        categories=(),
        age=(),
    ),
]
