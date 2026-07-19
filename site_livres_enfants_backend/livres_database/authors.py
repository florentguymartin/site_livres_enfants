from enum import StrEnum

class Author(StrEnum):
    AARON_BECKER = "Aaron Becker"
    DAVID_WIESNER = "David Wiesner"
    EMILY_ARNOLD_MCCULLOUGH = "Emily Arnold McCully"
    HELEN_OXENBURY = "Helen Oxenbury"
    KAZUO_IWAMURA = "Kazuo Iwamura"


author_descriptions: dict[Author, str] = {
    Author.DAVID_WIESNER: "David Wiesner est un auteur et illustrateur américain, célèbre pour ses livres pour enfants qui utilisent des illustrations innovantes et des récits visuels.",
    Author.KAZUO_IWAMURA: "Kazuo Iwamura est un auteur et illustrateur japonais, reconnu pour ses livres pour enfants qui mettent en avant la nature et les relations humaines.",
}