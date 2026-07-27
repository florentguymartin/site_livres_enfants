from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

karen_jameson_livres: list[Livre] = [
    Livre(
        titre="Au bois dormant",
        auteur=(Author.KAREN_JAMESON, Author.MARC_BOUTAVANT),
        couverture_path="au_bois_dormant.jpg",
        description="Un livre sur les animaux avant de dormir.",
        categories=(BooksCategory.POUR_REVER,),
        age=(BooksAge.AGE_0_1_ANS, BooksAge.AGE_2_3_ANS,)
    ),
]
