# -*- coding: utf-8 -*-
from words_image import get_keywords, save_image
import os

BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, "data")
IMAGE_DIR = os.path.join(BASE_DIR, "images")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

if __name__ == "__main__":
    words = get_keywords(DATA_DIR)
    for image in os.listdir(IMAGE_DIR):
        image_name = os.path.join(IMAGE_DIR, image)
        save_image(words, image_name, OUTPUT_DIR)
