from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

marcia_brown_livres: list[Livre] = [
    Livre(
        titre="La féticheuse",
        auteur=Author.MARCIA_BROWN,
        couverture_path="la_feticheuse.jpg",
        description=(
            "Illustrations d'un poème de Blaise Cendrars"
        ),
        categories=(),
        age=(BooksAge.AGE_4_5_ANS,)
        
    ),
]
