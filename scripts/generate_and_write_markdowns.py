# -*- coding: utf-8 -*-
import os
from site_livres_enfants_backend.livres_database import database
from site_livres_enfants_backend.config import root_directory
from site_livres_enfants_backend.livre import Livre, BooksCategory, LivreRendererMarkdown
from site_livres_enfants_backend.build_markdown import generate_author_pages, write_all_category_markdown, write_all_age_markdown
os.chdir(root_directory)

livres = database

if __name__ == "__main__":
    write_all_category_markdown(livres)

    write_all_age_markdown(livres)

    generate_author_pages(livres)