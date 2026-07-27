from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

julia_donaldson_livres: list[Livre] = [
    Livre(
        titre="Le Gruffalo",
        auteur=(Author.JULIA_DONALDSON, Author.AXEL_SCHEFFLER),
        couverture_path="der_grueffelo.jpg",
        description=(
            "La loi du plus fort est toujours la meilleure. Vraiment? "
            "La petite souris et le Gruffalo nous montrent qu'il n'en va pas toujours ainsi."
            "Un bon comique de répétition."
        ),
        categories=(BooksCategory.POUR_RIRE,),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS)
    ),
]
