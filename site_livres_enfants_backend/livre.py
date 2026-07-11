from typing import Optional
from pydantic import BaseModel, ConfigDict
from enum import Enum

class BooksCategory(Enum):
    GIRL_EMPOWERMENT = "girl_empowerment"
    LIVRES_SANS_IMAGE = "livres_sans_image"

class Livre (BaseModel):
    titre: str
    auteur: str
    couverture_path: Optional[str] = None
    categories: list[BooksCategory] = []
    description: str
    
    model_config = ConfigDict(extra='forbid') # at runtime raise an error if an extra field is present at init
