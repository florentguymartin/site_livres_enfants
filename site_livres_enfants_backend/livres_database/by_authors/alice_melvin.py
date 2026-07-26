from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

alice_melvin_livres: list[Livre] = [
    Livre(
        titre="Mit Maus im Wald",
        auteur=Author.ALICE_MELVIN,
        couverture_path="mit_maus_im_wald.jpg",
        # todo: description needs to be entered manually afterwards
        description=(
            "to be filled"
        ),
        categories=(),
        age=(),
    ),
]
