from site_livres_enfants_backend.livre import Livre, BooksCategory, BooksAge
from site_livres_enfants_backend.livres_database.authors import Author
from site_livres_enfants_backend.book_awards import PrixBolognaRagazzi

mitsumasa_anno_livres: list[Livre] = [
    Livre(
        titre="Ce jour-là...",
        auteur=Author.MITSUMASA_ANNO,
        couverture_path="ce_jour_la.jpg",
        description=(
            "Un voyage initiatique à travers l'Europe des siècles passés. "
            "Beaucoup de détails. "
            "Beaucoup de références artistiques qui m'échappent, mais il y a des explications à la fin."
        ),
        categories=(BooksCategory.LIVRES_SANS_TEXTE,),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS)
    ),
    Livre(
        titre="Sur les traces de Don Quichotte",
        auteur=Author.MITSUMASA_ANNO,
        couverture_path="sur_les_traces_de_don_quichotte.jpg",
        description=(
            "Même principe que 'ce jour-là...' en zoomant sur l'Espagne."
        ),
        categories=(BooksCategory.LIVRES_SANS_TEXTE,),
        age=(BooksAge.AGE_4_5_ANS,),
    ),
    Livre(
        titre="Dix petits amis déménagent",
        auteur=Author.MITSUMASA_ANNO,
        couverture_path="dix_petits_amis_demenagent.jpg",
        description=(
            "Un super livre pour une introduction en douceur au concept de soustraction (table de 10)."
        ),
        categories=(BooksCategory.LIVRES_SANS_TEXTE,),
        age=(BooksAge.AGE_4_5_ANS,),
    ),
    Livre(
        titre="Jeux de chapeaux",
        auteur=Author.MITSUMASA_ANNO,
        couverture_path="jeux_de_chapeau.jpg",
        description=(
            "Une introduction aux maths."
        ),
        categories=(),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS)
    ),
    Livre(
        titre="Jeux mathématiques",
        auteur=Author.MITSUMASA_ANNO,
        couverture_path="jeux_mathematiques.jpg",
        description=(
            "Une introduction aux maths. Tout en douceur ."
        ),
        categories=(),
        age=(BooksAge.AGE_4_5_ANS,)
    ),
    Livre(
        titre="Le Danemark d'Anderson",
        auteur=Author.MITSUMASA_ANNO,
        couverture_path="le_danemark_d_anderson.jpg",
        description=(
            "Un voyage à travers le Danemark, en suivant les traces d'Andersen."
        ),
        categories=(BooksCategory.LIVRES_SANS_TEXTE,),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS,)
    ),
    Livre(
        titre="Le loup, le crapaud et les trois petits cochons",
        auteur=Author.MITSUMASA_ANNO,
        couverture_path="le_loup_le_crapaud_et_les_trois_petits_cochons.jpg",
        description=(
            "Une introduction aux maths."
        ),
        categories=(),
        age=(BooksAge.AGE_4_5_ANS, )
    ),
    Livre(
        titre="Le pot magique",
        auteur=Author.MITSUMASA_ANNO,
        couverture_path="le_pot_magique.jpg",
        description=(
            "Expliquer le concept de factorielle avec des dessins. Pas sûr que ça marche. "
            "Mais c'est déjà beau d'essayer !"
        ),
        categories=(),
        age=()

    ),
    Livre(
        titre="Loup y es-tu?",
        auteur=Author.MITSUMASA_ANNO,
        couverture_path="loup_y_es_tu.jpg",
        description=(
            "Des illustrations d'un bois. "
            "Dans chaque page des animaux ou des visages se cachent dans les dessins. "
            "Enfants captivés !"
        ),
        categories=(BooksCategory.LIVRES_SANS_TEXTE,),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS)

    ),
    Livre(
        titre="Zwergenspuk",
        auteur=Author.MITSUMASA_ANNO,
        couverture_path="zwergenspuk.jpg",
        description=(
            "Un style très Escher. Avec plusieurs niveaux de compréhension. "
            "Unique dans son genre."
        ),
        categories=(BooksCategory.LIVRES_SANS_TEXTE,),
        age=(BooksAge.AGE_2_3_ANS, BooksAge.AGE_4_5_ANS,),
        awards=(
            PrixBolognaRagazzi(year=1972, additional_comment="Mention spéciale pour les enfants")
        ),
    ),
]
