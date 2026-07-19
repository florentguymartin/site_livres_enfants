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
    )
]
