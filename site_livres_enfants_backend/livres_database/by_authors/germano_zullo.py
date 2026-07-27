from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

germano_zullo_livres: list[Livre] = [
    Livre(
        titre="Ligne 135",
        auteur=(Author.GERMANO_ZULLO, Author.ALBERTINE),
        couverture_path="ligne_135.jpg",
        description=(
            "Une petite fille voyage en train de la ville à la campagne et se questionne sur le sens de la vie. "
            "Avec des illustrations très belles, poétiques et créatives."
        ),
        categories=(BooksCategory.POUR_REVER,),
        age=(BooksAge.AGE_4_5_ANS, BooksAge.AGE_2_3_ANS),
    ),
]
