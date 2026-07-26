from enum import StrEnum

class Author(StrEnum):
    AARON_BECKER = "Aaron Becker"
    ANNE_MARGOT_RAMSTEIN = "Anne-Margot Ramstein"
    ANTHONY_BROWN = "Anthony Browne"
    AURORE_PETIT = "Aurore Petit"
    AXEL_SCHEFFLER = "Axel Scheffler"
    CATI_BAUR = "Cati Baur"
    CHIAKI_OKADA = "Chiaki Okada"
    CHRIS_VAN_ALLSBURG = "Chris Van Allsburg"
    DAVID_ELLWAND = "David Ellwand"
    DAVID_WIESNER = "David Wiesner"
    EMILY_ARNOLD_MCCULLOUGH = "Emily Arnold McCully"
    GERDA_MULLER = "Gerda Muller"
    HELEN_OXENBURY = "Helen Oxenbury"
    JOERG_MUEHLE = "Jörg Mühle"
    JULIA_DONALDSON = "Julia Donaldson"
    KAREN_JAMESON = "Karen Jameson"
    KAZUO_IWAMURA = "Kazuo Iwamura"
    KO_OKADA = "Ko Okada"
    MARC_BOUTAVANT = "Marc Boutavant"
    MARIE_DORLEANS = "Marie Dorléans"
    MARIO_RAMOS = "Mario Ramos"
    MATTHIAS_AREGUI = "Matthias Aregui"
    MEM_FOX = "Mem Fox"
    MITSUMASA_ANNO = "Mitsumasa Anno"
    PAULINE_DELABROY_ALLARD = "Pauline Delabroy-Allard"
    STEPHANIE_BLAKE = "Stephanie Blake"
    THE_TJONG_KHING = "Thé Tjong-Khing"


author_descriptions: dict[Author, str] = {
    Author.ANTHONY_BROWN: (
        "Anthony Browne est un auteur et illustrateur britannique, "
        "connu pour ses livres pour enfants qui explorent des thèmes de l'imagination et de la réalité."
    ),
    Author.DAVID_WIESNER: (
        "David Wiesner est un auteur et illustrateur américain, "
        "célèbre pour ses livres pour enfants qui utilisent des illustrations innovantes et des récits visuels."
    ),
    Author.KAZUO_IWAMURA: (
        "Kazuo Iwamura est un auteur et illustrateur japonais, "
        "reconnu pour ses livres pour enfants qui mettent en avant la nature et les relations humaines."
    ),
    Author.MITSUMASA_ANNO: (
        "Mitsumasa Anno est un auteur et illustrateur japonais, "
        "célèbre pour ses livres pour enfants qui explorent des thèmes de la nature, "
        "du voyage, de l'art et des mathématiques."
        "Mitsumasa Anno est également connu pour son approche unique de la narration visuelle, "
        "incitant les jeunes lecteurs à interagir avec les illustrations et à découvrir des histoires cachées."
    ),
}