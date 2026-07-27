from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

philippe_corentin_livres: list[Livre] = [
    Livre(
        titre="Plouf!",
        auteur=Author.PHILIPPE_CORENTIN,
        couverture_path="plouf.jpg",
        description=(
            "Quand on voît quelque chose qui brille au fond d'un puit, faut réfléchir avant de sauter!"
        ),
        categories=(BooksCategory.POUR_RIRE,),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS),
    ),
]
