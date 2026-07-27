from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

the_tjong_khing_livres: list[Livre] = [
    Livre(
        titre="Waar is de taart?",
        auteur=Author.THE_TJONG_KHING,
        couverture_path="die_torte_ist_weg.jpg",
        description=(
            "Deux souris volent un gâteau d'anniversaire. "
            "Une course poursuite s'ensuit. "
            "Il y a plusieurs histoires en parallèle. "
            "C'est un super livre (sans texte), très interactif et qui permet de découvrir un nouveau détail à chaque lecture."
            "Non édité en français, mais comme il n'y a pas de texte, peu importe la langue d'édition. "
            "Disponible par exemple en néerlandais et allemand."
        ),
        categories=(BooksCategory.LIVRES_SANS_TEXTE,),
        age=(BooksAge.AGE_2_3_ANS,BooksAge.AGE_4_5_ANS,)
    ),
]
