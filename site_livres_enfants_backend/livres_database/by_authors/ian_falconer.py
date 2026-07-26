from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

ian_falconer_livres: list[Livre] = [
    Livre(
        titre="Olivia Reine des Princesses",
        auteur=Author.IAN_FALCONER,
        couverture_path="olivia_reine_des_princesses.jpg",
        # todo: description needs to be entered manually afterwards
        description=(
            "to be filled"
        ),
        categories=(),
        age=(),
    ),
]
