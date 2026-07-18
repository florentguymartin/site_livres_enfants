# -*- coding: utf-8 -*-
import os
from site_livres_enfants_backend.livres_database import database
from site_livres_enfants_backend.config import root_directory
from site_livres_enfants_backend.livre import Livre, BooksCategory, LivreRendererMarkdown
from site_livres_enfants_backend.build_markdown import write_category_markdown
os.chdir(root_directory)




livres = database

write_category_markdown(
    filename="girls_empowerment.md",
    title="Girls empowerment",
    category=BooksCategory.GIRL_EMPOWERMENT,
    category_description="Des livres où des filles et des femmes jouent le premier role et sont inspirantes.",
    livres=livres,
)

write_category_markdown(
    filename="livres_sans_image.md",
    title="Livres sans images",
    category=BooksCategory.LIVRES_SANS_IMAGE,
    category_description="Des livres sans images, pour stimuler l'imagination.",
    livres=livres,
)