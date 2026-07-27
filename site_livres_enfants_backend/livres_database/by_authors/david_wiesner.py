from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

david_wiesner_livres: list[Livre] = [
    Livre(
        titre="Le monde englouti",
        auteur=Author.DAVID_WIESNER,
        couverture_path="flotsam.jpg",
        description="Un livre sur l'imagination et la créativité.",
        categories=(BooksCategory.POUR_REVER, BooksCategory.LIVRES_SANS_TEXTE),
        age=(BooksAge.AGE_4_5_ANS,)
    ),
    Livre(
        titre="Chute libre",
        auteur=Author.DAVID_WIESNER,
        couverture_path="chute_libre.jpg",
        description=(
        "Comme toujours avec Davide Wiesner, beaucoup de poésie et de créativité. "
        "Un garçon s'endort avec un livre dans les bras, et qu'on suit dans ses rêves. "
        "À couper le souffle."
        ),
        categories=(BooksCategory.POUR_REVER, BooksCategory.LIVRES_SANS_TEXTE),
        age=(BooksAge.AGE_4_5_ANS, BooksAge.AGE_2_3_ANS),
    ),
    Livre(
        titre="Les trois cochons",
        auteur=Author.DAVID_WIESNER,
        couverture_path="les_trois_cochons.jpg",
        description=(
            "Une réinterprétation imaginative du conte classique."
        ),
        categories=(BooksCategory.LIVRES_SANS_TEXTE,),
        age=(BooksAge.AGE_4_5_ANS,),
    ),
    Livre(
        titre="Mardi",
        auteur=Author.DAVID_WIESNER,
        couverture_path="mardi.jpg",
        description=(
            "Un livre sur un mardi pas comme les autres."
        ),
        categories=(BooksCategory.LIVRES_SANS_TEXTE,),
        age=(BooksAge.AGE_4_5_ANS,),
    ),

]
