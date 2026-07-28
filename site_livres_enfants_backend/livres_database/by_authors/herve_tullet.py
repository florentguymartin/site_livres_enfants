from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author
from site_livres_enfants_backend.book_awards import PrixSorciere

herve_tullet_livres: list[Livre] = [
    Livre(
        titre="Un livre",
        auteur=Author.HERVE_TULLET,
        couverture_path="un_livre.jpg",
        description=(
            "Un livre super interactif pour apprendre couleur, formes et espace. "
            "Merci Justine !"
        ),
        categories=(),
        age=(BooksAge.AGE_0_1_ANS, BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS),
        awards=(PrixSorciere(year=2011, additional_comment="Catégorie tout-petits"))
    ),
]
