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
    Livre(
        titre="Le Carnaval des dragons",
        auteur=Author.MAX_DUCOS,
        couverture_path="le_carnaval_des_dragons.jpg",
        # todo: description needs to be entered manually afterwards
        description=(
            "to be filled"
        ),
        categories=(),
        age=(),
    ),
    Livre(
        titre="Vert secret",
        auteur=Author.MAX_DUCOS,
        couverture_path="vert_secret.jpg",
        # todo: description needs to be entered manually afterwards
        description=(
            "to be filled"
        ),
        categories=(),
        age=(),
    ),
    Livre(
        titre="Jeu de pist à Volubilis",
        auteur=Author.MAX_DUCOS,
        couverture_path="volubilis.jpg",
        # todo: description needs to be entered manually afterwards
        description=(
            "to be filled"
        ),
        categories=(),
        age=(),
    ),
]
