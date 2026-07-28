from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author
from site_livres_enfants_backend.book_awards import PrixBolognaRagazzi

anne_margot_ramstein_livres: list[Livre] = [
    Livre(
        titre="Avant Après",
        auteur=(Author.ANNE_MARGOT_RAMSTEIN, Author.MATTHIAS_AREGUI),
        couverture_path="avant_apres.jpg",
        description="Jour - Nuit, bourgeon - Fleur, vache - lait, etc.",
        categories=(BooksCategory.LIVRES_SANS_TEXTE,),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS,),
        awards=(
            PrixBolognaRagazzi(year=2015, additional_comment="non fiction, gagnant")
        ),
    ),
]
