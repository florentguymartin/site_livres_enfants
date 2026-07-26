from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

stephanie_blake_livres: list[Livre] = [
    Livre(
        titre="Caca boudin",
        auteur=Author.STEPHANIE_BLAKE,
        couverture_path="caca_boudin.jpg",
        description=(
            "Tout est dans le titre."
            "C'est pas du Shakespeare, mais tout le monde rigole." 
        ),
        categories=(BooksCategory.POUR_RIRE,),
        age=(BooksAge.AGE_2_3_ANS,)
    ),
]
