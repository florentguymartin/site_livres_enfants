from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

tomi_ungerer_livres: list[Livre] = [
    Livre(
        titre="Les trois brigands",
        auteur=Author.TOMI_UNGERER,
        couverture_path="les_trois_brigands.jpg",
        # todo: description needs to be entered manually afterwards
        description=(
            "to be filled"
        ),
        categories=(),
        age=(),
    ),
]
