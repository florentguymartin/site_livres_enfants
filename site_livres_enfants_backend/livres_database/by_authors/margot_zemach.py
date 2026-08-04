from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

margot_zemach_livres: list[Livre] = [
    Livre(
        titre="Ça pourrait être pire",
        auteur=Author.MARGOT_ZEMACH,
        couverture_path="ca_pourrait_etre_pire.jpg",
        description=(
            "Un conte Yiddish. "
            "Absurde. Très (très) drôle. "
            "Et philosophique. "
        ),
        categories=(BooksCategory.POUR_RIRE,),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS)
    ),
]
