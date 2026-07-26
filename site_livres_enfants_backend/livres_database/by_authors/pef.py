from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

pef_livres: list[Livre] = [
    Livre(
        titre="La belle lisee poire du prince de Motordu",
        auteur=Author.PEF,
        couverture_path="la_belle_lisse_poire_du_prince_de_motordu.jpg",
        description=(
            "Un livre plein d'humour sur les jeux de mots et les sonorités."
        ),
        categories=(BooksCategory.POUR_RIRE,),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS,)
    ),
]
