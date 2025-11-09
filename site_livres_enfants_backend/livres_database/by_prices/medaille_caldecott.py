from site_livres_enfants_backend.livre import Livre


medaille_caldecott_books: list[Livre] = []

juliette_et_bellini = Livre(
    titre="Juliette et Bellini",
    auteur="Emily Arnold McCuly",
    girl_empowerment="""Ce livre est extraordinaire.""",
    couverture_path="juliette_et_bellini.jpg",
)

medaille_caldecott_books.append(juliette_et_bellini)

voyage = Livre(
    titre="Voyage",
    auteur="Aaron Becker",
    girl_empowerment="La petite fille mène l'action. C'est elle qui sauve le roi. C'est elle qui a la curiosité d'initier l'histoire qui nous est racontée."
)

medaille_caldecott_books.append(voyage)