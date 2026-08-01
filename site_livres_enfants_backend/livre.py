from typing import Optional
from pydantic import BaseModel, ConfigDict
from enum import Enum, StrEnum
from site_livres_enfants_backend.livres_database.authors import Author
from .book_awards import BookAward

class BooksCategory(StrEnum):
    """
    Catégories de livres
    """
    GIRL_EMPOWERMENT = "girls_empowerment"
    LIVRES_SANS_TEXTE = "livres_sans_texte"
    POUR_RIRE = "pour_rire"
    POUR_REVER = "pour_rever"

class BooksAge(StrEnum):
    """
    Tranches d'âge
    """
    AGE_0_1_ANS = "0_1_ans"
    AGE_2_3_ANS = "2_3_ans"
    AGE_4_5_ANS = "4_5_ans"

# mapping category to (title, description)
category_descriptions: dict[BooksCategory, tuple[str, str]] = {
    BooksCategory.GIRL_EMPOWERMENT: (
        "Girl Empowerment", 
        (
            "Sois belle et tais-toi."
            "Dans un monde idéal, en 2026, on ne devrait pas parler de girl empowerment."
            "Dans un monde idéal il y aurait plein de livres pour enfants où un personnage féminin peut s'apparenter à un *role model*."
            "Malheureusement, mon expérience personnelle me dit que ce n'est pas le cas."
            "Et malheureusement, les livres présentés dans cette page se comptent sur les doigts d'une main."
            "Raison de plus pour les mettre en avant."
        ),
        ),
    BooksCategory.LIVRES_SANS_TEXTE: (
        "Livres sans texte", 
        "Des livres sans texte, avec seulement des images, pour stimuler l'imagination.",
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
    """ 
    Représente un livre.
    """
    titre: str
    auteur: Author | tuple[Author, ...]
    couverture_path: str | None | list[str] = None
    categories: tuple[BooksCategory, ...] = ()
    description: str
    age: tuple[BooksAge, ...] = ()
    awards: tuple[BookAward, ...] | BookAward | None = None

    model_config = ConfigDict(extra='forbid', arbitrary_types_allowed=True) # at runtime raise an error if an extra field is present at init

    def get_author_as_str(self) -> str:
        if isinstance(self.auteur, tuple):
            return "_".join([auteur.value for auteur in self.auteur])
        return self.auteur.value

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
        if livre.couverture_path is not None:
            if isinstance(livre.couverture_path, list):
                couverture_path_list = livre.couverture_path
            elif isinstance(livre.couverture_path, str):
                couverture_path_list = [livre.couverture_path]
            else:
                raise TypeError(f"Invalid type for couverture_path, expected None, str or list[str] but got {type(livre.couverture_path)}")
            for img_path in couverture_path_list:
                lines.append(f"![Screenshot]({img_folder}/" + img_path + "){ width=\"100\" }")
            lines.append("")
        lines.append(livre.description)
        lines.append("")
        if livre.awards is not None:
            if isinstance(livre.awards, BookAward):
                awards_list = (livre.awards,)
            elif isinstance(livre.awards, tuple):
                awards_list = livre.awards
            for award in awards_list:
                lines.append(f"{award.to_str()}  ")
            lines.append("")
        return "\n".join(lines)