from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

christelle_saquet_livres: list[Livre] = [
    Livre(
        titre="Les histoires du soir de Litouho",
        auteur=Author.CHRISTELLE_SAQUET,
        couverture_path="les_histoires_du_soir_de_litouho.jpg",
        description=(
            "Une histoire sur les vertus de savoir lire tout seul. "
            "Et sur la filouterie de maître hibou !"
            "Merci Matou !"
        ),
        categories=(),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS),
    ),
]
