from enum import StrEnum

class Author(StrEnum):
    AARON_BECKER = "Aaron Becker"
    ANTHONY_BROWN = "Anthony Browne"
    CATI_BAUR = "Cati Baur"
    DAVID_WIESNER = "David Wiesner"
    EMILY_ARNOLD_MCCULLOUGH = "Emily Arnold McCully"
    HELEN_OXENBURY = "Helen Oxenbury"
    JOERG_MUEHLE = "Jörg Mühle"
    KAREN_JAMESON = "Karen Jameson"
    KAZUO_IWAMURA = "Kazuo Iwamura"
    MARC_BOUTAVANT = "Marc Boutavant"
    MEM_FOX = "Mem Fox"
    PAULINE_DELABROY_ALLARD = "Pauline Delabroy-Allard"


author_descriptions: dict[Author, str] = {
    Author.ANTHONY_BROWN: "Anthony Browne est un auteur et illustrateur britannique, connu pour ses livres pour enfants qui explorent des thèmes de l'imagination et de la réalité.",
    Author.DAVID_WIESNER: "David Wiesner est un auteur et illustrateur américain, célèbre pour ses livres pour enfants qui utilisent des illustrations innovantes et des récits visuels.",
    Author.KAZUO_IWAMURA: "Kazuo Iwamura est un auteur et illustrateur japonais, reconnu pour ses livres pour enfants qui mettent en avant la nature et les relations humaines.",
}