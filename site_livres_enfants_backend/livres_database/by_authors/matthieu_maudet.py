from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

matthieu_maudet_livres: list[Livre] = [
    Livre(
        titre="Occupé",
        auteur=Author.MATTHIEU_MAUDET,
        couverture_path="occupe.jpg",
        description=(
            "Les toilettes sont occupées. Et la file d'attente s'allonge. "
            "Mais gare à la chute!"
        ),
        categories=(BooksCategory.POUR_RIRE,),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS),
    ),
]
