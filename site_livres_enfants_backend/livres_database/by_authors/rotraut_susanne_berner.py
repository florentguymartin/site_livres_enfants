from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

rotraut_susanne_berner_livres: list[Livre] = [
    Livre(
        titre="Le livre de l'été",
        auteur=Author.ROTRAUT_SUSANNE_BERNER,
        couverture_path="sommer_wimmelbuch.jpg",
        description=(
            "Dans la série de Rotraut Susanne Berner. "
            "Des livres avec pleins de détails sur la vie quotidienne. "
            "Super pour discuter avec les enfants et les aider à développer leur language."
        ),
        categories=(BooksCategory.LIVRES_SANS_TEXTE,),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS),
    ),
]
