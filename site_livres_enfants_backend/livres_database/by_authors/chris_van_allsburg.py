from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

chris_van_allsburg_livres: list[Livre] = [
    Livre(
        titre="Boréal-Express",
        auteur=Author.CHRIS_VAN_ALLSBURG,
        couverture_path="boreal_express.jpg",
        description=(
            "La nuit de Noël. Un petit garçon." 
            "Un train sorti de nulle part. La vraie magie de Noël."
        ),
        categories=(BooksCategory.POUR_REVER,),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS)
    ),
]
