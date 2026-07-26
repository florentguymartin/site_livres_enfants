from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

joerg_muehle_livres: list[Livre] = [
    Livre(
        titre="Au bain petit lapin",
        auteur=Author.JOERG_MUEHLE,
        couverture_path="au_bain_petit_lapin.jpg",
        description="Une histoire courte, simple, ludique et efficace pour les petits.",
        categories=(),
        age=(BooksAge.AGE_0_1_ANS, BooksAge.AGE_2_3_ANS,)
    ),
    Livre(
        titre="Au lit petit lapin",
        auteur=Author.JOERG_MUEHLE,
        couverture_path="au_lit_petit_lapin.jpg",
        description="Une histoire douce et apaisante pour l'heure du coucher.",
        categories=(),
        age=(BooksAge.AGE_0_1_ANS, BooksAge.AGE_2_3_ANS,),
    ),
    Livre(
        titre="On joue, Petit Lapin!",
        auteur=Author.JOERG_MUEHLE,
        couverture_path="on_joue_petit_lapin.jpg",
        # todo: description needs to be entered manually afterwards
        description=(
            "to be filled"
        ),
        categories=(),
        age=(),
    ),
]
