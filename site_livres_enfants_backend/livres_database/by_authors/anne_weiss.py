from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

anne_weiss_livres: list[Livre] = [
    Livre(
        titre="Les petits bonheurs de pré",
        auteur=Author.ANNE_WEISS,
        couverture_path="les_petits_bonheurs_du_pre.jpg",
        description=(
            "to be filled"
        ),
        categories=(),
        age=()
        #todo: description needs to be entered manually afterwards
    ),
]
