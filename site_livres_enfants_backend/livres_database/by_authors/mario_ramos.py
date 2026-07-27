from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

mario_ramos_livres: list[Livre] = [
    Livre(
        titre="Au lit, petit monstre!",
        auteur=Author.MARIO_RAMOS,
        couverture_path="au_lit_petit_monstre.jpg",
        description="Les enfants sont parfois des petits monstres, surtout au moment du coucher. Mais le monstre n'est pas toujours celui qu'on croit...",
        categories=(BooksCategory.POUR_RIRE,),
        age=(BooksAge.AGE_2_3_ANS,)
    ),
]
