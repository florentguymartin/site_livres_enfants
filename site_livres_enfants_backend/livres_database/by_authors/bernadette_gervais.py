from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

bernadette_gervais_livres: list[Livre] = [
    Livre(
        titre="Des trucs comme ci, des trucs comme ça",
        auteur=Author.BERNADETTE_GERVAIS,
        couverture_path="des_trucs_comme_ci_des_trucs_comme_ca.jpg",
        description=(
            "to be filled"
        ),
        categories=(),
        age=()
        #todo: description needs to be entered manually afterwards
    ),
]
