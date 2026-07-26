from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

gerda_muller_livres: list[Livre] = [
    Livre(
        titre="Boucle d'or et les trois ours",
        auteur=Author.GERDA_MULLER,
        couverture_path="boucle_d_or_et_les_trois_ours.jpg",
        description=(
            "Des belles illustrations et une approche moderne de cette histoire classique."
        ),
        categories=(),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS)
    ),
]
