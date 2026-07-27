from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

noe_carlain_livres: list[Livre] = [
    Livre(
        titre="Prout de Mammouth",
        auteur=Author.NOE_CARLAIN,
        couverture_path="prout_de_mammouth.jpg",
        description=(
            "Des animaux et des prouts. " 
            "C'est pas du Shakespeare, et je me rapelle avoir entendu des 'Oh mais arretez avec ce livre'! "
            "Mais merci Pauline pour les séances de rigolade !"
        ),
        categories=(BooksCategory.POUR_RIRE,),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS),
    ),
]
