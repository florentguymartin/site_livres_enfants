from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author
from site_livres_enfants_backend.livre import BooksAge, BooksCategory
albertine_livres: list[Livre] = [
    Livre(
        titre="La Rumeur de Venise",
        auteur=(Author.ALBERTINE, Author.GERMANO_ZULLO),
        couverture_path="la_rumeur_de_venise.jpg",
        description=(
            "Un livre sans texte, qui illustre comment la rumeur passe d'une maison à l'autre."
            "Et tout ça en voyageant à travers Venise."
        ),
        categories=(BooksCategory.LIVRES_SANS_TEXTE,),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS,)
    ),
    Livre(
        titre="Marta et la bicyclette",
        auteur=(Author.ALBERTINE, Author.GERMANO_ZULLO),
        couverture_path="marta_et_la_bicyclette.jpg",
        description=(
            "Une vache qui fait de la bicyclette."
        ),
        categories=(),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS)
        
    ),
]
