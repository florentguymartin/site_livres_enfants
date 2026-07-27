from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

janosch_livres: list[Livre] = [
    Livre(
        titre="Je te guérirai, dit l'ours",
        auteur=Author.JANOSCH,
        couverture_path="ich_mach_dich_gesund_sagte_der_baer.jpg",
        description=(
            "Le tigre est malade et son ami ours lui promet de le guérir. "
            "Un beau livre sur l'amitié. "
            "Un classique en Allemagne."
        ),
        categories=(),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS)
    ),
]
