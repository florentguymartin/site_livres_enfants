from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

haruo_yamashita_livres: list[Livre] = [
    Livre(
        titre="Les souris à la plage",
        auteur=(Author.KAZUO_IWAMURA, Author.HARUO_YAMASHITA),
        couverture_path="les_souris_a_la_plage.jpg",
        description=(
            "Une histoire de souris qui partent en vacances à la plage."
        ),
        categories=(),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS),
    ),
]
