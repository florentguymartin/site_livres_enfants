# -*- coding: utf-8 -*-
import os
from site_livres_enfants_backend.livres_database import database
from site_livres_enfants_backend.config import root_directory
from site_livres_enfants_backend.livre import Livre, BooksCategory, LivreRendererMarkdown
from site_livres_enfants_backend.build_markdown import write_all_author_pages, write_all_category_pages_md, write_all_age_pages_md
os.chdir(root_directory)

livres = database

if __name__ == "__main__":
    write_all_category_pages_md(livres)

    write_all_age_pages_md(livres)

    write_all_author_pages(livres)