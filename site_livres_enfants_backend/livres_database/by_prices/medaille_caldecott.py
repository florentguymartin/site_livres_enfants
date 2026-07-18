from site_livres_enfants_backend.livre import Livre, BooksCategory  
from site_livres_enfants_backend.livres_database.authors import Author


medaille_caldecott_books: list[Livre] = []

juliette_et_bellini = Livre(
    titre="Juliette et Bellini",
    auteur=Author.EMILY_ARNOLD_MCCULLOUGH,
    description="""Ce livre est extraordinaire.""",
    couverture_path="juliette_et_bellini.jpg",
    categories=[BooksCategory.GIRL_EMPOWERMENT]
)

medaille_caldecott_books.append(juliette_et_bellini)

voyage = Livre(
    titre="Voyage",
    auteur=Author.AARON_BECKER,
    description="La petite fille mène l'action. C'est elle qui sauve le roi. C'est elle qui a la curiosité d'initier l'histoire qui nous est racontée.",
    categories=[
        BooksCategory.GIRL_EMPOWERMENT,
        BooksCategory.LIVRES_SANS_IMAGE,
    ]
)

medaille_caldecott_books.append(voyage)