from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

chiaki_okada_livres: list[Livre] = [
    Livre(
        titre="C'est toi le Printemps?",
        auteur=(Author.CHIAKI_OKADA, Author.KO_OKADA,),
        couverture_path="bist_du_der_fruehling.jpg",
        description=(
            "Le benjamin des lapins entend beaucoup parler du printemps."
            "Mais c'est quoi le Printemps? Un livre avec de belles illustrations pour découvrir cette saison."
        ),
        categories=(BooksCategory.POUR_REVER,),
        age=(BooksAge.AGE_2_3_ANS,)
    ),
]
