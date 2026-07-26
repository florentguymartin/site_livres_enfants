from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

olivier_tallec_livres: list[Livre] = [
    Livre(
        titre="Est-ce qu'il dort?",
        auteur=Author.OLIVIER_TALLEC,
        couverture_path="est_ce_qu_il_dort.jpg",
        description=(
            "Un petit oiseau est par terre. Est-ce qu'il dort? " 
            "En fait non. "
            "Un livre qui essaye d'aborder le sujet de la mort tout en douceur. "
        ),
        categories=(),
        age=(BooksAge.AGE_4_5_ANS,)
    ),
]
