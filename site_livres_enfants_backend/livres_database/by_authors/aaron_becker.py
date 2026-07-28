from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author

aaron_becker_livres: list[Livre] = [
    Livre(
    titre="Voyage | Quest | Imagine, encore...",
    auteur=Author.AARON_BECKER,
    couverture_path=["voyage.jpg", "quest.jpg", "imagine_encore.jpg"],
    description=(
        "Une trilogie très originale qui suit les aventures d'une petite fille dans un mondes imaginaire."
        "À l'aide de son crayon, elle crée des objets, des outils, des animaux qui lui permet d'avancer dans son aventure."
        "Bien qu'il n'y ait pas de texte, dans chaque livre le scénario est très bien ficelé et captivant pour les enfants."
        "C'est la petite fille qui mène l'action. "
        "C'est elle qui sauve le roi. "
        "Et c'est elle qui a la curiosité d'initier l'histoire qui nous est racontée."
    ),
    categories=(BooksCategory.GIRL_EMPOWERMENT, BooksCategory.LIVRES_SANS_TEXTE),
    age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS),
    ),
    # Livre(
    # titre="Voyage",
    # auteur=Author.AARON_BECKER,
    # couverture_path="voyage.jpg",
    # description=(
    #     "La petite fille mène l'action. "
    #     "C'est elle qui sauve le roi. "
    #     "C'est elle qui a la curiosité d'initier l'histoire qui nous est racontée."
    # ),
    # categories=(
    #     BooksCategory.GIRL_EMPOWERMENT,
    #     BooksCategory.LIVRES_SANS_TEXTE,
    # ),
    # age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS,),
    # ),
    # Livre(
    #     titre="Quest",
    #     auteur=Author.AARON_BECKER,
    #     couverture_path="quest.jpg",
    #     description=(
    #         "Deuxième livre de la série (après 'Voyage'). "
    #         "Une histoire à la Indiana Jones où la petite fille est aidée par un garçon dans une quête colorée. "
    #     ),
    #     categories=(BooksCategory.LIVRES_SANS_TEXTE,),
    #     age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS,),
    # ),
    # Livre(
    #     titre="Imagine, encore...",
    #     auteur=Author.AARON_BECKER,
    #     couverture_path="imagine_encore.jpg",
    #     description=(
    #         "Troisième et dernier livre de la série (après 'Voyage' et 'Quest'). "
    #         "Le papa essaye de ramener la petite fille dans le monde réel, au début sans succès. "
    #         "Quelques pérégrinations plus tard, la morale c'est que les adultes sont parfois de bon conseil."
    #     ),
    #     categories=(BooksCategory.LIVRES_SANS_TEXTE,),
    #     age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS,),
    # ),
    
    Livre(
        titre="The tree and the River",
        auteur=Author.AARON_BECKER,
        couverture_path="the_tree_and_the_river.jpg",
        description=(
            "Une histoire sur le temps qui passe et son effet sur les paysages, les villes et les hommes."
        ),
        categories=(BooksCategory.LIVRES_SANS_TEXTE,),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS,),
    ),
]
