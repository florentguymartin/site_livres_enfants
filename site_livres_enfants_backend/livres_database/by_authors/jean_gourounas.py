from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

jean_gourounas_livres: list[Livre] = [
    Livre(
        titre="Grosse Légume",
        auteur=Author.JEAN_GOUROUNAS,
        couverture_path="grosse_legume.jpg",
        description=(
            "À mourir de rire. "
            "L'histoire d'un ver qui s'enfile des légumes. "
            "Attention, pour que le charme opère, il faut que le lecteur lise le livre de manière rythmique. "
            "Les kids en redemandent!"
        ),
        categories=(BooksCategory.POUR_RIRE,),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS)
    ),
]
