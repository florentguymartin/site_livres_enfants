from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

byron_barton_livres: list[Livre] = [
    Livre(
        titre="Les camions",
        auteur=Author.BYRON_BARTON,
        couverture_path="les_camions.jpg",
        description=(
            "Des illustrations minimalistes très bien pour les tout petits."
        ),
        categories=(),
        age=(BooksAge.AGE_0_1_ANS,),
    ),
    Livre(
        titre="Ma maison",
        auteur=Author.BYRON_BARTON,
        couverture_path="ma_maison.jpg",
        description=(
            "Des illustrations minimalistes très bien pour les tout petits."
        ),
        categories=(),
        age=(BooksAge.AGE_0_1_ANS,),
    ),
]
