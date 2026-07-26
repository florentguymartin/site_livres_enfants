from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

noe_carlain_livres: list[Livre] = [
    Livre(
        titre="Prout de Mammouth",
        auteur=Author.NOE_CARLAIN,
        couverture_path="prout_de_mammouth.jpg",
        # todo: description needs to be entered manually afterwards
        description=(
            "to be filled"
        ),
        categories=(),
        age=(),
    ),
]
