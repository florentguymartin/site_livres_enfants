from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

claude_boujon_livres: list[Livre] = [
    Livre(
        titre="La brouille",
        auteur=Author.CLAUDE_BOUJON,
        couverture_path="la_brouille.jpg",
        description=(
            "Deux petits lapins voisins, qui commencent à se brouiller pour de broutilles. "
            "Mais un renard va remettre de l'ordre dans tout ça."
        ),
        categories=(BooksCategory.POUR_RIRE,),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS,)
    ),
    Livre(
        titre="La chaise bleue",
        auteur=Author.CLAUDE_BOUJON,
        couverture_path="la_chaise_bleue.jpg",
        description=(
            "Nous donnons trop de jouets aux enfants. " 
            "Less is more. "
            "La preuve par la chaise"
        ),
        categories=(),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS,)
    ),
]
