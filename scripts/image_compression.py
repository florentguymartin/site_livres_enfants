""" 
Script to compress images in a directory.

In this script, we will compress all images in a specified directory and save them to a target directory.
"""

from PIL import Image
from site_livres_enfants_backend.config import root_directory
import os

JPEG_IMG_QUALITY = 10


def compress_image(src_image_path: str, target_image_path: str, quality: int):
    im = Image.open(src_image_path)
    im.save(target_image_path, "JPEG", quality=quality)


if __name__ == "__main__":
    high_quality_image_dirpath = os.path.join(root_directory, "site_livres_enfants_mkdocs", "docs", "img_high_quality")
    target_image_dirpath = os.path.join(root_directory, "site_livres_enfants_mkdocs", "docs", "img")
    
    # list filenames in the dir
    high_quality_image_filenames = os.listdir(high_quality_image_dirpath)
    
    # Compress and save images
    for filename in high_quality_image_filenames:
        src_image_path = os.path.join(high_quality_image_dirpath, filename)
        target_image_path = os.path.join(target_image_dirpath, filename)
        compress_image(src_image_path=src_image_path, target_image_path=target_image_path, quality=JPEG_IMG_QUALITY)


