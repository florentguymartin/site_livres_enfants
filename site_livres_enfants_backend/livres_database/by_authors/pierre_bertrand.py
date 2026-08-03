from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

pierre_bertrand_livres: list[Livre] = [
    Livre(
        titre="Cornebidouille",
        auteur=Author.PIERRE_BERTRAND,
        couverture_path="cornebidouille.jpg",
        description=(
            "to be filled"
        ),
        categories=(),
        age=()
        #todo: description needs to be entered manually afterwards
    ),
]
