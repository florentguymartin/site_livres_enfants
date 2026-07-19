from typing import Optional
from pydantic import BaseModel, ConfigDict
from enum import Enum, StrEnum
from site_livres_enfants_backend.livres_database.authors import Author

class BooksCategory(StrEnum):
    GIRL_EMPOWERMENT = "girls_empowerment"
    LIVRES_SANS_IMAGE = "livres_sans_image"
    POUR_RIRE = "pour_rire"
    POUR_REVER = "pour_rever"

class BooksAge(StrEnum):
    AGE_0_1_ANS = "0_1_ans"
    AGE_2_3_ANS = "2_3_ans"
    AGE_4_5_ANS = "4_5_ans"

# mapping category to (title, description)
category_descriptions: dict[BooksCategory, tuple[str, str]] = {
    BooksCategory.GIRL_EMPOWERMENT: (
        "Girl Empowerment", 
        "Des livres où des filles et des femmes jouent le premier role et sont inspirantes.",
        ),
    BooksCategory.LIVRES_SANS_IMAGE: (
        "Livres sans image", 
        "Des livres sans images, pour stimuler l'imagination.",
    ),
    BooksCategory.POUR_RIRE: (
        "Pour rire", 
        "Des livres pour rire et s'amuser.",
    ),
    BooksCategory.POUR_REVER: (
        "Pour rêver", 
        "Des livres pour rêver et s'évader.",
    ),
}


# mapping age to descriptions:
age_descriptions: dict[BooksAge,tuple[str, str]] = {
    BooksAge.AGE_0_1_ANS: (
        "0-1 ans", 
        "Des livres pour les tout-petits.",
    ),
    BooksAge.AGE_2_3_ANS: (
        "2-3 ans", 
        "Des livres pour les enfants de 2 à 3 ans.",
    ),
    BooksAge.AGE_4_5_ANS: (
        "4-5 ans", 
        "Des livres pour les enfants de 4 à 5 ans.",
    ),
}

class Livre (BaseModel):
    titre: str
    auteur: Author | tuple[Author, ...]
    couverture_path: Optional[str] = None
    categories: tuple[BooksCategory, ...] = ()
    description: str
    age: tuple[BooksAge, ...] = ()

    model_config = ConfigDict(extra='forbid') # at runtime raise an error if an extra field is present at init

class LivreRendererMarkdown:

    def render_markdown(
        self, 
        livre: Livre,
        img_folder: str | None = None,
        ) -> str:
        """Render a Livre instance as a Markdown string.

        Args:
            livre (Livre): The Livre instance to render.

        Returns:
            str: The rendered Markdown string.
        """
        if img_folder is None:
            img_folder = "./img"
        lines = []
        if isinstance(livre.auteur, tuple):
            auteur_as_str = " et ".join([auteur.value for auteur in livre.auteur])
        else:
            auteur_as_str = livre.auteur.value
        lines.append(f"## {livre.titre} (*{auteur_as_str}*)")
        lines.append("")
        if livre.couverture_path:
            # specify image size explicitely to be at most 300 pixels
            lines.append(f"![Screenshot]({img_folder}/" + livre.couverture_path + "){ width=\"100\" }")
            lines.append("")
        lines.append(livre.description)
        lines.append("")
        return "\n".join(lines)