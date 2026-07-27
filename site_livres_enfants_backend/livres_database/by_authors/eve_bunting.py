from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

eve_bunting_livres: list[Livre] = [
    Livre(
        titre="Le petit bateau de petit ours",
        auteur=Author.EVE_BUNTING,
        couverture_path="le_petit_bateau_de_petit_ours.jpg",
        description=(
            "Une histoire de barques qui finissent par être trop petites quand on grandit trop. "
            "Mignon et bon enfant."
        ),
        categories=(),
        age=(BooksAge.AGE_2_3_ANS,),
    ),
]
