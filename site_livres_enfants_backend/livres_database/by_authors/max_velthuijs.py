from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

max_velthuijs_livres: list[Livre] = [
    Livre(
        titre="Petit-Bond est amoureux",
        auteur=Author.MAX_VELTHUIJS,
        couverture_path="petit_bond_est_amoureux.jpg",
        # todo: description needs to be entered manually afterwards
        description=(
            "to be filled"
        ),
        categories=(),
        age=(),
    ),
]
