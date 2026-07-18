from typing import Optional
from pydantic import BaseModel, ConfigDict
from enum import Enum
from site_livres_enfants_backend.livres_database.authors import Author

class BooksCategory(Enum):
    GIRL_EMPOWERMENT = "girl_empowerment"
    LIVRES_SANS_IMAGE = "livres_sans_image"
    POUR_RIRE = "pour_rire"
    POUR_REVER = "pour_rever"

class Livre (BaseModel):
    titre: str
    auteur: Author
    couverture_path: Optional[str] = None
    categories: tuple[BooksCategory, ...] = ()
    description: str
    
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
        lines.append(f"## {livre.titre} (*{livre.auteur}*)")
        lines.append("")
        if livre.couverture_path:
            # specify image size explicitely to be at most 300 pixels
            lines.append(f"![Screenshot]({img_folder}/" + livre.couverture_path + "){ width=\"100\" }")
            lines.append("")
        lines.append(livre.description)
        lines.append("")
        return "\n".join(lines)