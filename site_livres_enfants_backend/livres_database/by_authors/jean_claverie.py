from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author
from site_livres_enfants_backend.book_awards import PrixSorciere

jean_claverie_livres: list[Livre] = [
    Livre(
        titre="L'art du pot",
        auteur=(Author.JEAN_CLAVERIE, Author.MICHELE_NIKLY),
        couverture_path="l_art_du_pot.jpg",
        description=(
            "Un super livre pour démystifier le pot. "
            "Très drole, très vrai, et de jolis dessins"
        ),
        categories=(BooksCategory.POUR_RIRE,),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS,),
        awards=(PrixSorciere(year=1991, additional_comment="Catégorie tout-petits")),
    ),
]
