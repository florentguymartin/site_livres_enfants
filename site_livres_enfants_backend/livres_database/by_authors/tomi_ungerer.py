from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

tomi_ungerer_livres: list[Livre] = [
    Livre(
        titre="Les trois brigands",
        auteur=Author.TOMI_UNGERER,
        couverture_path="les_trois_brigands.jpg",
        description=(
            "Trois brigands décident de voler tous les voyageurs de la route. "
            "Mais ils vont rencontrer une petite fille qui va changer leur vie. "
            "Un classique de la littérature jeunesse."
        ),
        categories=(),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS,),
    ),
]
