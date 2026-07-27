from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

suzy_lee_livres: list[Livre] = [
    Livre(
        titre="La Vague",
        auteur=Author.SUZY_LEE,
        couverture_path="la_vague.jpg",
        description=(
            "Une petite fille, une plage, des vagues. "
            "Rira bien qui rira le dernier !"
        ),
        categories=(BooksCategory.LIVRES_SANS_TEXTE,),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS),
    ),
]
