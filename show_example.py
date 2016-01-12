# -*- coding: utf-8 -*-
from words_image import get_keywords, show_image
import os

BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, "data")
IMAGE_DIR = os.path.join(BASE_DIR, "images")
IMAGE_PATH = os.path.join(IMAGE_DIR, "tony.png")

if __name__ == "__main__":
    words = get_keywords(DATA_DIR)
    show_image(words, IMAGE_PATH)