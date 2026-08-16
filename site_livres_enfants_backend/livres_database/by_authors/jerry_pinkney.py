from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author
from site_livres_enfants_backend.book_awards import MedailleCaldecott

jerry_pinkney_livres: list[Livre] = [
    Livre(
        titre="Le lion et la souris",
        auteur=Author.JERRY_PINKNEY,
        couverture_path="le_lion_et_la_souris.jpg",
        description=(
            "La fable d'Ésope illustrée par Jerry Pinkney, sans texte. "
            "De très belles illustrations et une morale qui traverse les millénaires."
        ),
        categories=(BooksCategory.LIVRES_SANS_TEXTE,),
        age=(BooksAge.AGE_0_1_ANS, BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS),
        awards=(MedailleCaldecott(year=2010, additional_comment="Gagnant"))
    ),
]
