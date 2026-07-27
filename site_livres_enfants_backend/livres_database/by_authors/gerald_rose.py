from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

gerald_rose_livres: list[Livre] = [
    Livre(
        titre="Le tapis en peau de tigre",
        auteur=Author.GERALD_ROSE,
        couverture_path="le_tapis_en_peau_de_tigre.jpg",
        # todo: description needs to be entered manually afterwards
        description=(
            "to be filled"
        ),
        categories=(),
        age=(),
    ),
]
