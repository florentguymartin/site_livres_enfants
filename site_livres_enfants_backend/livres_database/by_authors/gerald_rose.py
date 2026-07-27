from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

gerald_rose_livres: list[Livre] = [
    Livre(
        titre="Le tapis en peau de tigre",
        auteur=Author.GERALD_ROSE,
        couverture_path="le_tapis_en_peau_de_tigre.jpg",
        description=(
            "Comme quoi les tigres ne sont pas toujours à envier. "
            "Mais tout en bien qui finit bien !"
        ),
        categories=(BooksCategory.POUR_RIRE,),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS),
    ),
]
