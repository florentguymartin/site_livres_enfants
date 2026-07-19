from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

david_wiesner_livres: list[Livre] = [
    Livre(
        titre="Le monde englouti",
        auteur=Author.DAVID_WIESNER,
        couverture_path="flotsam.jpg",
        description="Un livre sur l'imagination et la créativité.",
        categories=(BooksCategory.POUR_REVER, BooksCategory.LIVRES_SANS_IMAGE),
        age=(BooksAge.AGE_4_5_ANS,)
    ),

]
