from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

marie_dorleans_livres: list[Livre] = [
    Livre(
        titre="Course épique",
        auteur=Author.MARIE_DORLEANS,
        couverture_path="course_epique.jpg",
        description=(
            "Les course à Longchamps c'est bien mais c'est pas très marrant. "
            "Ce livre permet d'inverser la tendance!"

        ),
        categories=(BooksCategory.POUR_RIRE,),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS)
    ),
]
