from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

claude_ponti_livres: list[Livre] = [
    Livre(
        titre="Adèle et la Pele",
        auteur=Author.CLAUDE_PONTI,
        couverture_path="adele_et_la_pele.jpg",
        description=(
            "Le troisième volet de la série Adèle. "
            "Adèle a grandi, mais l'imagination de l'auteur n'a pas d'âge."
        ),
        categories=(BooksCategory.LIVRES_SANS_TEXTE,),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS)

    ),
    Livre(
        titre="Adèle s'en mêle",
        auteur=Author.CLAUDE_PONTI,
        couverture_path="adele_s_en_mele.jpg",
        description=(
            "Le deuxième volet de la série Adèle. "
            "Adèle rentre dans le livre."
        ),
        categories=(BooksCategory.LIVRES_SANS_TEXTE,),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS)

    ),
    Livre(
        titre="L'album d'Adèle",
        auteur=Author.CLAUDE_PONTI,
        couverture_path="l_album_d_adele.jpg",
        description=(
            "Le premier volet de la série Adèle. "
            "Un livre sans image, où on découvre de nouveaux détails à chaque lecture. "
            ""
        ),
        categories=(BooksCategory.LIVRES_SANS_TEXTE,),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS)
    ),
]
