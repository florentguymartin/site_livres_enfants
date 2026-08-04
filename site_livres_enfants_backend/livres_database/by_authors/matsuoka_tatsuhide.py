from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

matsuoka_tatsuhide_livres: list[Livre] = [
    Livre(
        titre="Saute",
        auteur=Author.MATSUOKA_TATSUHIDE,
        couverture_path="saute.jpg",
        description=(
            "Des animaux qui sauntent. C'est pas du Shakespeare. Mais ça fait rire les petits. "
        ),
        categories=(BooksCategory.POUR_RIRE,),
        age=(BooksAge.AGE_0_1_ANS, BooksAge. AGE_2_3_ANS),
    ),
]
