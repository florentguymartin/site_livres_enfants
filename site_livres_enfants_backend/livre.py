from pydantic import BaseModel, ConfigDict

class Livre (BaseModel):
    titre: str
    auteur: str
    couverture_path: str | None = None
    livres_sans_image: str | None = None
    girl_empowerment: str | None = None
    
    model_config = ConfigDict(extra='forbid') # at runtime raise an error if an extra field is present at init
