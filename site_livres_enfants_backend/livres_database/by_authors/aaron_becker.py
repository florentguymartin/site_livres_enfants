from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

aaron_becker_livres: list[Livre] = [
    Livre(
    titre="Voyage",
    auteur=Author.AARON_BECKER,
    description=(
        "La petite fille mène l'action. "
        "C'est elle qui sauve le roi. "
        "C'est elle qui a la curiosité d'initier l'histoire qui nous est racontée."
    ),
    categories=(
        BooksCategory.GIRL_EMPOWERMENT,
        BooksCategory.LIVRES_SANS_TEXTE,
    ),
    age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS,),
    ),
]
