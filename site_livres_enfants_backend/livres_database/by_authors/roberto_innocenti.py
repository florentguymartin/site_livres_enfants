from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

roberto_innocenti_livres: list[Livre] = [
    Livre(
        titre="La maison",
        auteur=Author.ROBERTO_INNOCENTI,
        couverture_path="la_maison.jpg",
        description=(
            "Une très belle histoire qui donne une perspective sur l'histoire du XXe siècle (en Italie) "
            "à travers les yeux d'une maison."
        ),
        age=(BooksAge.AGE_4_5_ANS,)
    ),
]
