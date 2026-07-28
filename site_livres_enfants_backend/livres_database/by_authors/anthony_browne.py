from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author
from site_livres_enfants_backend.book_awards import PrixBolognaRagazzi, PrixSorciere

anthony_browne_livres: list[Livre] = [
    Livre(
        titre="Une histoire à quatre voix",
        auteur=Author.ANTHONY_BROWN,
        couverture_path="une_histoire_a_quatre_voix.jpg",
        description=(
            "Une histoire racontée par quatre personnages différents, chacun avec sa propre perspective. "
            "Très drole, et offre une réflexion sur la subjectivité des points de vue. "
            "Les illustrations sont bourrées de détails en arrière-plan: à chaque lecture on découvre un nouveau détail. "
        ),
        categories=(BooksCategory.POUR_RIRE,),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS,),
        awards=(
            PrixSorciere(year=1999, additional_comment="Catégorie albums")
        )
    ),
    Livre(
        titre="Anna et le gorille",
        auteur=(Author.ANTHONY_BROWN),
        couverture_path="anna_et_le_gorille.jpg",
        description="Une petite fille, un anniversaire, un gorille.",
        categories=(BooksCategory.POUR_REVER,),
        age=(BooksAge.AGE_2_3_ANS,)
    ),
    Livre(
        titre="Le garçon, le chien et la mer",
        auteur=Author.ANTHONY_BROWN,
        couverture_path="le_garcon_le_chien_et_la_mer.jpg",
        description=(
            "Un petit frère qui s'ennuie sans son grand frère. "
            "Un chien qui ne demande qu'à sortir. "
            "Une belle morale."
        ),
        categories=(),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS,),
    ),
    Livre(
        titre="Le tunnel",
        auteur=Author.ANTHONY_BROWN,
        couverture_path="le_tunnel.jpg",
        description=(
            "Une soeur et un grand frère qui ne s'entendent pas. "
            "Une soeur qui est introvertie et se fait chambrer par son frère. "
            "Mais c'est la grande soeur qui surmonte sa peur et va sauver son frere. "
            "Comme souvent avec Anthony Browne l'arrière-plan est truffés de détails extra-ordinaires."
        ),
        categories=(BooksCategory.GIRL_EMPOWERMENT,),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS,),
    ),
    Livre(
        titre="Ourson et la ville",
        auteur=Author.ANTHONY_BROWN,
        couverture_path="ourson_et_la_ville.jpg",
        description=(
            "Une méchante brigade séquestre des animaux. Heureusement Ourson va tout faire pour les sauver."
        ),
        categories=(),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS,),
    ),
    Livre(
        titre="À calicochon",
        auteur=Author.ANTHONY_BROWN,
        # couverture_path="a_calicochon.jpg",
        description=(
            "On n'est plus dans les années 60."
            "Enfin pas encore chez les Porchon, mais ça ne va pas durer."
            "Un livre drôle pour rappeler qu'à une époque les mamans avaient un rôle différent et pas enviable."
        ),
        categories=(),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS),
        awards=(
            PrixBolognaRagazzi(year=1987, additional_comment="Mention spéciale pour les enfants")
        )   
    )
]
