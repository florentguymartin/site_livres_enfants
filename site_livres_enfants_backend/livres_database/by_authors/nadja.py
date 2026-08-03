from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

nadja_livres: list[Livre] = [
    Livre(
        titre="Chien bleu",
        auteur=Author.NADJA,
        couverture_path="chien_bleu.jpg",
        description=(
            "to be filled"
        ),
        categories=(),
        age=()
        #todo: description needs to be entered manually afterwards
    ),
]
