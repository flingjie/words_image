# -*- coding: utf-8 -*-
from words_image import get_content, show_image
import os

BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, "data")
IMAGE_DIR = os.path.join(BASE_DIR, "images")
IMAGE_PATH = os.path.join(IMAGE_DIR, "tony.png")

if __name__ == "__main__":
    content = get_content(DATA_DIR)
    show_image(content, IMAGE_PATH)