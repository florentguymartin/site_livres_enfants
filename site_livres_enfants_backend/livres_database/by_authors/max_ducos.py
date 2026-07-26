from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

max_ducos_livres: list[Livre] = [
    Livre(
        titre="L'ange disparu",
        auteur=Author.MAX_DUCOS,
        couverture_path="l_ange_disparu.jpg",
        description=(
            "Une visite au musée qui sort de l'ordinaire. "
        ),
        categories=(BooksCategory.POUR_REVER,),
        age=(BooksAge.AGE_2_3_ANS,)
    ),
]
