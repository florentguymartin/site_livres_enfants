from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

jerry_pinkney_livres: list[Livre] = [
    Livre(
        titre="Le lion et la souris",
        auteur=Author.JERRY_PINKNEY,
        couverture_path="le_lion_et_la_souris.jpg",
        # todo: description needs to be entered manually afterwards
        description=(
            "to be filled"
        ),
        categories=(),
        age=(),
    ),
]
