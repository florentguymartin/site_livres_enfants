from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author
from site_livres_enfants_backend.livre import BooksCategory, BooksAge

alain_le_saux_livres: list[Livre] = [
    Livre(
        titre="Petit Musée",
        auteur=Author.ALAIN_LE_SAUX,
        couverture_path="petit_musee.jpg",
        description=(
            "Un imagier avec des tableaux de peinture. "
        ),
        categories=(BooksCategory.LIVRES_SANS_TEXTE,),
        age=(BooksAge.AGE_4_5_ANS, BooksAge.AGE_2_3_ANS,)
    ),
]
