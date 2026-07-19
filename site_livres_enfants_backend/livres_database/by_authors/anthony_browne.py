from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

anthony_browne_livres: list[Livre] = [
    Livre(
        titre="Anna et le gorille",
        auteur=(Author.ANTHONY_BROWN),
        couverture_path="anna_et_le_gorille.jpg",
        description="Une petite fille, un anniversaire, un gorille.",
        categories=(BooksCategory.POUR_REVER,),
        age=(BooksAge.AGE_2_3_ANS,)
    ),
]
