from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

author_livres: list[Livre] = [
    Livre(
        titre="titre",
        auteur=Author.KAZUO_IWAMURA,
        couverture_path="img_filename",
        description=(
            "Un livre sur les liens familiaux et la nature."
        ),
        categories=(BooksCategory.POUR_REVER,),
        age=(BooksAge.AGE_2_3_ANS,)
    ),
]
