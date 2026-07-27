from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

christelle_saquet_livres: list[Livre] = [
    Livre(
        titre="Les histoires du soir de Litouho",
        auteur=Author.CHRISTELLE_SAQUET,
        couverture_path="les_histoires_du_soir_de_litouho.jpg",
        # todo: description needs to be entered manually afterwards
        description=(
            "to be filled"
        ),
        categories=(),
        age=(),
    ),
]
