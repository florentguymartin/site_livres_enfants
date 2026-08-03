from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

paul_zelinsky_livres: list[Livre] = [
    Livre(
        titre="Grigrigredinmenufretin",
        auteur=Author.PAUL_ZELINKSKY,
        couverture_path="grigrigredin_menufretin.jpg",
        description=(
            "Les livres de Paul Zelinksy sont des oeuvres d'art."
            "La narration de l'histoire des frères Grimm n'est pas très moderne, mais les illustrations "
            "de Zelinksy sont magnifiques et plaisent aux enfants."
        ),
        categories=(),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS)
    ),
    Livre(
        titre="Raiponce",
        auteur=Author.PAUL_ZELINKSKY,
        couverture_path="raiponce.jpg",
        description=(
            "to be filled"
        ),
        categories=(),
        age=()
        #todo: description needs to be entered manually afterwards
    ),
]
