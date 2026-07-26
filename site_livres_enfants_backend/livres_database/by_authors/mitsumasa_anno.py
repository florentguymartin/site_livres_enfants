from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

mitsumasa_anno_livres: list[Livre] = [
    Livre(
        titre="Ce jour-là...",
        auteur=Author.MITSUMASA_ANNO,
        couverture_path="ce_jour_la.jpg",
        description=(
            "Un voyage initiatique à travers l'Europe des siècles passés. "
            "Beaucoup de détails. "
            "Beaucoup de références artistiques qui m'échappent, mais il y a des explications à la fin."
        ),
        categories=(BooksCategory.LIVRES_SANS_TEXTE,),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS)
    ),
    Livre(
        titre="Sur les traces de Don Quichotte",
        auteur=Author.MITSUMASA_ANNO,
        couverture_path="sur_les_traces_de_don_quichotte.jpg",
        # todo: description needs to be entered manually afterwards
        description=(
            "to be filled"
        ),
        categories=(),
        age=(),
    ),
    Livre(
        titre="Zwergenspuk",
        auteur=Author.MITSUMASA_ANNO,
        couverture_path="zwergenspuk.jpg",
        # todo: description needs to be entered manually afterwards
        description=(
            "to be filled"
        ),
        categories=(),
        age=(),
    ),
]
