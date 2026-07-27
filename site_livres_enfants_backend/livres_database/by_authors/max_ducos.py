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
        description=(
            "Comment transormer un échec en succès. "
        ),
        categories=(),
        age=(BooksAge.AGE_4_5_ANS,),
    ),
    Livre(
        titre="Vert secret",
        auteur=Author.MAX_DUCOS,
        couverture_path="vert_secret.jpg",
        description=(
            "Du grand Max Ducos qui offre là une histoire complexe et captivante. "
            "Un scénario super pour les enfants, servi avec de belles illustrations."
        ),
        categories=(),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS,),
    ),
    Livre(
        titre="Jeu de pist à Volubilis",
        auteur=Author.MAX_DUCOS,
        couverture_path="volubilis.jpg",
        description=(
            "Un jeu de piste captivant dans dans une maison d'architecte. "
            "Un scénario complexe mais qui se suit bien par les enfants."
        ),
        categories=(),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS,),
    ),
]
