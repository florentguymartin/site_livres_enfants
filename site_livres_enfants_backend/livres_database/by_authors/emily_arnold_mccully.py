from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

emily_arnold_mccully_livres: list[Livre] = [
    Livre(
    titre="Juliette et Bellini",
    auteur=Author.EMILY_ARNOLD_MCCULLOUGH,
    description=(
        "Juliette est une petite fille curieuse, courageuse, persévérante et émouvante. "
        "Quand elle fait la rencontre du célebre finambule Bellini, elle est tout de suite fascinée par son art. "
        "À force de détermination, elle finit par attitrer l'attention de Bellini qui l'entraîne. "
        "Spoiler: Et le jour où Bellini se retrouve en difficulté sur le fil, en pleine nuit et dans le vide, c'est Juliette qui vient le sauver "
        "et nour offre une dernière page sous les étoiles à couper le souffle. "
        "Go Juliette! "
        "Un livre magnifique."
    ),
    couverture_path="juliette_et_bellini.jpg",
    categories=(BooksCategory.GIRL_EMPOWERMENT,),
    age = (BooksAge.AGE_4_5_ANS,)
),
]
