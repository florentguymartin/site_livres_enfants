from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

josse_goffin_livres: list[Livre] = [
    Livre(
        titre="Oh",
        auteur=Author.JOSSE_GOFFIN,
        couverture_path="oh.jpg",
        description=(
            "Pas de texte. Des pages qu'on peut déplier. "
            "Avant de déplier la page on a une suggestion qui s'avère incorrecte une fois la page dépliée. "
            "Très ludique et éducatif. "
        ),
        categories=(BooksCategory.LIVRES_SANS_TEXTE,),
        age=(BooksAge.AGE_0_1_ANS, BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS),
    ),
]
