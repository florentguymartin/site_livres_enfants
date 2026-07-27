from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

adrien_albert_livres: list[Livre] = [
    Livre(
        titre="Un bisou pour mon frère",
        auteur=Author.ADRIEN_ALBERT,
        couverture_path="un_bisou_pour_mon_frere.jpg",
        description=(
            "Deux lapins, deux frères. "
            "Une histoire qui part dans tous les sens, mais ils sont tellement mignons que ça passe!"
        ),
        categories=(),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS,),
    ),
]
