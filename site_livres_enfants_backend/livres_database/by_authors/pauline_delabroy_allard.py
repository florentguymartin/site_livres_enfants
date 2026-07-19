from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

pauline_delabroy_allard_livres: list[Livre] = [
    Livre(
        titre="Aller bon train",
        auteur=(Author.PAULINE_DELABROY_ALLARD, Author.CATI_BAUR),
        couverture_path="aller_bon_train.jpg",
        description="Un super livre avant un voyage en train.",
        categories=(),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS)
    ),
]
