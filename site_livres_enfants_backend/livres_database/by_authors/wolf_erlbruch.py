from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

wolf_erlbruch_livres: list[Livre] = [
    Livre(
        titre="La grande question",
        auteur=Author.WOLF_ERLBRUCH,
        couverture_path="la_grande_question.jpg",
        description=(
            "Une introduction à la philosophie pour les enfants. "
        ),
        categories=(),
        age=(BooksAge.AGE_4_5_ANS,)
    ),
]
