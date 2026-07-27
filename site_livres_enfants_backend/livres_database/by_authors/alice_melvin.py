from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

alice_melvin_livres: list[Livre] = [
    Livre(
        titre="Souris des bois - Une année dans la forêt",
        auteur=Author.ALICE_MELVIN,
        couverture_path="mit_maus_im_wald.jpg",
        
        description=(
            "On suit une souris dans ses bois de Janvier à Décembre, "
            "avec de très belles illustrations."
        ),
        categories=(),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS,),
    ),
]
