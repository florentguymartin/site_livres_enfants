from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

catherine_zarcate_livres: list[Livre] = [
    Livre(
        titre="Les poulets guerriers",
        auteur=Author.CATHERINE_ZARCATE,
        couverture_path="les_poulets_guerriers.jpg",
        description=(
            "Attention: ce livre nécessite de se donner la peine de chanter la 'Chanson des poulet guerriers'. "
            "Si vous trouvez le bon rythme, succès assuré !"
        ),
        categories=(BooksCategory.POUR_RIRE,),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS,),
    ),
]
