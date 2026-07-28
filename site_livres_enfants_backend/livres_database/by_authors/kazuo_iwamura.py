from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

kazuo_iwamura_livres: list[Livre] = [
    Livre(
        titre="L'hiver de la famille souris",
        auteur=Author.KAZUO_IWAMURA,
        couverture_path="l_hiver_de_la_famille_souris.jpg",
        description=(
            "La famille sourise est décidément très bricoleuse. "
            "Les souris fabriquent elle-même leur luge. "
        ),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS)
    ),
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
    ),
    Livre(
        titre="Le pique-nique de la famille Souris",
        auteur=Author.KAZUO_IWAMURA,
        couverture_path="familie_maus_macht_picknick.jpg",
        description=(
            "Tour est dans le titre."
        ),
        categories=(),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS)
    ),
    Livre(
        titre="La famille Souris et le potiron",
        auteur=Author.KAZUO_IWAMURA,
        couverture_path="la_famille_souris_et_le_potiron.jpg",
        description=(
            "Une superbe histoire pour donner une introduction à la botanique."
        ),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS),
    ),
    Livre(
        titre="La famille souris prépare le nouvel an",
        auteur=Author.KAZUO_IWAMURA,
        couverture_path="la_famille_souris_prepare_le_nouvel_an.jpg",
        description=(
            "Le nouvel an au Japon, ça se mérite (du moins d'après cette histoire). "
        ),
    ),
    Livre(
        titre="La fête d'automne de la famille souris",
        auteur=Author.KAZUO_IWAMURA,
        couverture_path="la_fete_dautomne_de_la_famille_souris.jpg",
        description=(
            "Sur cet album Kazuo Iwamura lache la bride! Très beau comme toujours avec lui."
        ),
    ),
    Livre(
        titre="La lessive de la famille souris",
        auteur=Author.KAZUO_IWAMURA,
        couverture_path="la_lessive_de_la_famille_souris.jpg",
        description=(
            "La magie de Kazuo Iwamura qui transforme une histoire banale (la lessive) en un moment poétique."
        ),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS),
    ),
    Livre(
        titre="Le train des souris",
        auteur=Author.KAZUO_IWAMURA,
        couverture_path="hurra_der_maeuszug_ist_da.jpg",
        description=(
            "Pour motiver les souris pour la rentrée des classes, la maman souris a une idée: "
            "suggérer des rails jusqu'à l'école. " 
            "Mais le chemin est semé d'embûches. "
        ),
        categories=(),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS)
    ),
    Livre(
        titre="Le petit déjeuner de la famille Souris",
        auteur=Author.KAZUO_IWAMURA,
        couverture_path="le_petit_dejeuner_de_la_famille_souris.jpg",
        description=(
            "Tout est dans le titre. Très belle histoire. "
        ),
        categories=(),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS),
    ),
    Livre(
        titre="Le piano des bois",
        auteur=Author.KAZUO_IWAMURA,
        couverture_path="le_piano_des_bois.jpg",
        description=(
            "Une belle histoire sur la musique et la nature."
        ),
        categories=(),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS),
    ),
    Livre(
        titre="Quand dormez-vous?",
        auteur=Author.KAZUO_IWAMURA,
        couverture_path="nachts_wenn_alle_schlaffen.jpg",
        description=(
            "Nic, Nac et Noc les écureuils vont la découverte du décalage horaire avec les hiboux. "
            "Très mignon comme d'habitude avec Kazuo Iwamura."
        ),
        categories=(),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS),
    ),
    Livre(
        titre="Tout est rouge",
        auteur=Author.KAZUO_IWAMURA,
        couverture_path="tout_est_rouge.jpg",
        description=(
            "Nic, Nac et Noc nous font découvrir les couleurs de l'Automne. " 
            "Simple et très beau."
        ),
        categories=(),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS),
    ),
    Livre(
        titre="Un orage d'été",
        auteur=Author.KAZUO_IWAMURA,
        couverture_path="un_orage_d_ete.jpg",
        description=(
            "Les enfants sont toujours impressionés, on pourrait dire fascinés, par les orages d'été. "
            "On peut compter sur Kazuo Iwamura pour traîter le sujet avec une histoire limpide et de très belles illustrations."
        ),
        categories=(),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS),
    ),
]
