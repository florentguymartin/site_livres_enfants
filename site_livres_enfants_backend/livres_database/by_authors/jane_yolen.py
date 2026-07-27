from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

jane_yolen_livres: list[Livre] = [
    Livre(
        titre="Un appel dans la nuit",
        auteur=Author.JANE_YOLEN,
        couverture_path="un_appel_dans_la_nuit.jpg",
        description=(
            "Partir la nuit observer le hibou. Une belle histoire et de jolies illustrations."
        ),
        categories=(),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS),
    ),
]
