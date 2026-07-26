from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

aaron_becker_livres: list[Livre] = [
    Livre(
    titre="Voyage",
    auteur=Author.AARON_BECKER,
    couverture_path="voyage.jpg",
    description=(
        "La petite fille mène l'action. "
        "C'est elle qui sauve le roi. "
        "C'est elle qui a la curiosité d'initier l'histoire qui nous est racontée."
    ),
    categories=(
        BooksCategory.GIRL_EMPOWERMENT,
        BooksCategory.LIVRES_SANS_TEXTE,
    ),
    age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS,),
    ),
    Livre(
        titre="Imagine, encore...",
        auteur=Author.AARON_BECKER,
        couverture_path="imagine_encore.jpg",
        # todo: description needs to be entered manually afterwards
        description=(
            "to be filled"
        ),
        categories=(),
        age=(),
    ),
    Livre(
        titre="Quest",
        auteur=Author.AARON_BECKER,
        couverture_path="quest.jpg",
        # todo: description needs to be entered manually afterwards
        description=(
            "to be filled"
        ),
        categories=(),
        age=(),
    ),
    Livre(
        titre="The tree and the River",
        auteur=Author.AARON_BECKER,
        couverture_path="the_tree_and_the_river.jpg",
        # todo: description needs to be entered manually afterwards
        description=(
            "to be filled"
        ),
        categories=(),
        age=(),
    ),
]
