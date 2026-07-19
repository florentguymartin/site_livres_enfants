from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

helen_oxenburry_livres: list[Livre] = [
    Livre(
        titre="2 petites mains et 2 petits pieds",
        auteur=(Author.MEM_FOX, Author.HELEN_OXENBURY),
        couverture_path="2_petites_mains_et_2_petits_pieds.jpg",
        description="Un livre sur la diversité des bébés.",
        categories=(),
        age=(BooksAge.AGE_0_1_ANS, BooksAge.AGE_2_3_ANS,)
    ),
]
