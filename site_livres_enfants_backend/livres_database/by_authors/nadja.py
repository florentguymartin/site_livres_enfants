from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

nadja_livres: list[Livre] = [
    Livre(
        titre="Chien bleu",
        auteur=Author.NADJA,
        couverture_path="chien_bleu.jpg",
        description=(
            "Une très belle histoire sur l'amitié entre une petite fille et un chien bleu. "
        ),
        categories=(BooksCategory.POUR_REVER,),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS)

    ),
]
