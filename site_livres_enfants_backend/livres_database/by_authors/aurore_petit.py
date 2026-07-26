from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

aurore_petit_livres: list[Livre] = [
    Livre(
        titre="Bébé ventre",
        auteur=Author.AURORE_PETIT,
        couverture_path="bebe_ventre.jpg",
        description="Comment un petit garçon de 3/4 ans prépare la venue d'une petite soeur.",
        categories=(BooksCategory.POUR_REVER,),
        age=(BooksAge.AGE_2_3_ANS,)
    ),
]
