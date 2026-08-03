from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

alain_le_saux_livres: list[Livre] = [
    Livre(
        titre="Petit Musée",
        auteur=Author.ALAIN_LE_SAUX,
        couverture_path="petit_musee.jpg",
        description=(
            "to be filled"
        ),
        categories=(),
        age=()
        #todo: description needs to be entered manually afterwards
    ),
]
