from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

david_ellwand_livres: list[Livre] = [
    Livre(
        titre="Beaucoup de beaux bébés",
        auteur=Author.DAVID_ELLWAND,
        couverture_path="beaucoup_de_beaux_bebes.jpg",
        description="Des photos de bébés. Un livre pour les tout-tout-petits.",
        categories=(BooksCategory.POUR_REVER,),
        age=(BooksAge.AGE_0_1_ANS,)
    ),
]
