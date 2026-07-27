from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

emily_arnold_mccully_livres: list[Livre] = [
    Livre(
    titre="Juliette et Bellini",
    auteur=Author.EMILY_ARNOLD_MCCULLOUGH,
    description="""Ce livre est extraordinaire.""",
    couverture_path="juliette_et_bellini.jpg",
    categories=(BooksCategory.GIRL_EMPOWERMENT,),
    age = (BooksAge.AGE_4_5_ANS,)
),
]
