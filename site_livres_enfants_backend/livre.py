from typing import Optional
from pydantic import BaseModel, ConfigDict

class Livre (BaseModel):
    titre: str
    auteur: str
    couverture_path: Optional[str] = None
    livres_sans_image: Optional[str] = None
    girl_empowerment: Optional[str] = None
    
    model_config = ConfigDict(extra='forbid') # at runtime raise an error if an extra field is present at init
