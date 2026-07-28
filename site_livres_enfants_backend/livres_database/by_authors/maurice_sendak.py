from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author
from site_livres_enfants_backend.book_awards import MedailleCaldecott

maurice_sendak_livres: list[Livre] = [
    Livre(
        titre="Max et les Maximonstres",
        auteur=Author.MAURICE_SENDAK,
        couverture_path="max_et_les_maximonstres.jpg",
        description=(
            "Un classique de la littérature enfantine, qui aborde les thèmes de l'imagination et de la rébellion."
        ),
        categories=(BooksCategory.POUR_REVER,),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS),
        awards=(
            MedailleCaldecott(year=1964)
        ),
    ),
]
