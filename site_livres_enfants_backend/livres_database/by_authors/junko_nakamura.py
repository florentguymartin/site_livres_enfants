from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

junko_nakamura_livres: list[Livre] = [
    Livre(
        titre="La visite",
        auteur=Author.JUNKO_NAKAMURA,
        couverture_path="la_visite.jpg",
        description=(
            "Des illustrations très très belles. "
            "Pas de texte, et une histoire qui laisse place à de nombreuses interprétations. "
            "Après 20 lectures, on ne se lasse pas."
        ),
        categories=(BooksCategory.POUR_REVER, BooksCategory.LIVRES_SANS_TEXTE,),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS),
    ),
]
