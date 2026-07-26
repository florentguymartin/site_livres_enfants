from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

jill_murphy_livres: list[Livre] = [
    Livre(
        titre="Enfin la paix",
        auteur=Author.JILL_MURPHY,
        couverture_path="enfin_la_paix.jpg",
        description=(
            "Papa ours veut dormir. Mais ça ne se passe pas toujours comme prévu."
        ),
        categories=(BooksCategory.POUR_RIRE,),
        age=(BooksAge.AGE_2_3_ANS,)
    ),
]
