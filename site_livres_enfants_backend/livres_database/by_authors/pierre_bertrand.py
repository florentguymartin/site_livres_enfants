from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

pierre_bertrand_livres: list[Livre] = [
    Livre(
        titre="Cornebidouille",
        auteur=Author.PIERRE_BERTRAND,
        couverture_path="cornebidouille.jpg",
        description=(
            "*Pierre, mange ta soupe. Nan j'veux pas!* "
            "Une histoire drôle sur la résistance à l'autorité parentale. "
        ),
        categories=(),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS,)
        
    ),
]
