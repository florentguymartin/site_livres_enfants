from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

claude_ponti_livres: list[Livre] = [
    Livre(
        titre="Adèle et la Pele",
        auteur=Author.CLAUDE_PONTI,
        couverture_path="adele_et_la_pele.jpg",
        description=(
            "to be filled"
        ),
        categories=(),
        age=()
        #todo: description needs to be entered manually afterwards
    ),
    Livre(
        titre="Adèle s'en mêle",
        auteur=Author.CLAUDE_PONTI,
        couverture_path="adele_s_en_mele.jpg",
        description=(
            "to be filled"
        ),
        categories=(),
        age=()
        #todo: description needs to be entered manually afterwards
    ),
    Livre(
        titre="L'album d'Adèle",
        auteur=Author.CLAUDE_PONTI,
        couverture_path="l_album_d_adele.jpg",
        description=(
            "to be filled"
        ),
        categories=(),
        age=()
        #todo: description needs to be entered manually afterwards
    ),
]
