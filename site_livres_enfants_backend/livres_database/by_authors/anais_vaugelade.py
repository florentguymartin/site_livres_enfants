from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

anais_vaugelade_livres: list[Livre] = [
    Livre(
        titre="Le secret",
        auteur=Author.ANAIS_VAUGELADE,
        couverture_path="le_secret.jpg",
        description=(
            "'Non je veux pas te dire' dit la poule au chat. Alors le chat, va se forger son propre secret. "
            "Une belle histoire qui part un peu dans tous les sens, sur fond de quête initiatique."
        ),
        categories=(),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS,),
    ),
]
