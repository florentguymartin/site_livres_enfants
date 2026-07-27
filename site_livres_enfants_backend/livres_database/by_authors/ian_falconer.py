from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

ian_falconer_livres: list[Livre] = [
    Livre(
        titre="Olivia Reine des Princesses",
        auteur=Author.IAN_FALCONER,
        couverture_path="olivia_reine_des_princesses.jpg",
        description=(
            "Toutes les petites filles rêvent de princesse. "
            "Se pamer devant le preux et fort chevalier. "
            "Être habillées toutes pareilles avec des tutus roses. "
            "Euh... vraiment ?! "
            "En tout cas pas Olivia !"
            "Merci Olivia !"
        ),
        categories=(BooksCategory.GIRL_EMPOWERMENT,),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS),
    ),
]
