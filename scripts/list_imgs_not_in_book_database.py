import os

from site_livres_enfants_backend.livres_database import database
from site_livres_enfants_backend.utils import project_root_dir_path 

list_of_images_in_database = [
    livre.couverture_path for livre in database if isinstance(livre.couverture_path, str)
]
for livre in database:
    if isinstance(livre.couverture_path, list):
        list_of_images_in_database.extend(livre.couverture_path)

# list files in site_livres_enfants_mkdocs/docs/img
list_of_image_filenames = os.listdir(os.path.join(project_root_dir_path, "site_livres_enfants_mkdocs", "docs", "img"))
delta = list(set(list_of_image_filenames) - set(list_of_images_in_database))

if len(delta) == 0:
    print("All images in site_livres_enfants_mkdocs/docs/img appear in the database")
else:
    print("Images not found in the database:")
    for img in delta:
        print(f" - {img}")