from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

kazuo_iwamura_livres: list[Livre] = [
    Livre(
        titre="La famille souris dîne au clair de lune",
        auteur=Author.KAZUO_IWAMURA,
        couverture_path="la_famille_souris_dine_au_clair_de_lune.jpg",
        description="Un livre sur les liens familiaux et la nature.",
        categories=(BooksCategory.POUR_REVER,),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS)
    ),
    Livre(
        titre="La famille souris et la racine geante",
        auteur=Author.KAZUO_IWAMURA,
        couverture_path="la_famille_souris_et_la_racine_geante.jpg",
        description="Une histoire sur la nature.",
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS)
    ),
    Livre(
        titre="À table",
        auteur=Author.KAZUO_IWAMURA,
        couverture_path="a_table.jpg",
        description="Les oiseaux ne mangent pas la même chose que les écureuils.",
        categories=(BooksCategory.POUR_REVER,),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS)
    ),
    Livre(
        titre="C'est déjà le Printemps!",
        auteur=Author.KAZUO_IWAMURA,
        couverture_path="c_est_deja_le_printemps.jpg",
        description=(
            "Que devient la neige au Printemps? "
            "Une très belle histoire, beaucoup de poésie, et une très belle rencontre au milieu du lac."
        ),
        categories=(BooksCategory.POUR_REVER,),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS)
    ),
    Livre(
        titre="Vive la neige",
        auteur=Author.KAZUO_IWAMURA,
        couverture_path="die_schlittenfahrt.jpg",
        description=(
            "Un peu de neige, c'est l'occasion idéale pour sortir la luge "
            "et permettre aux adultes de retrouver une âme d'enfants."
        ),
        categories=(BooksCategory.POUR_REVER,),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS)
    )
]
