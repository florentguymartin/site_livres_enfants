from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

martin_waddell_livres: list[Livre] = [
    Livre(
        titre="Tu ne dors pas, petit ours?",
        auteur=Author.MARTIN_WADDELL,
        couverture_path="tu_ne_dors_pas_petit_ours.jpg",
        description=(
            "Un livre dont certains parents se rappeleront. "
            "Très mignon, et en tant que parent, pas trop dur de s'identifier."
        ),
        categories=(),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS),
    ),
]
