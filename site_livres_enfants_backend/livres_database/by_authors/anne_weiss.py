from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

anne_weiss_livres: list[Livre] = [
    Livre(
        titre="Les petits bonheurs de pré",
        auteur=(Author.ANNE_WEISS, Author.PASCALE_ESTELLON,),
        couverture_path="les_petits_bonheurs_du_pre.jpg",
        description=(
            "Un imagier champêtre, avec de très très belles illustrations."
        ),
        categories=(),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS)
        
    ),
]
