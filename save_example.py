# -*- coding: utf-8 -*-
from words_image import get_content, save_image
import os

BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, "data")
IMAGE_DIR = os.path.join(BASE_DIR, "images")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

if __name__ == "__main__":
    content = get_content(DATA_DIR)
    for image in os.listdir(IMAGE_DIR):
        image_name = os.path.join(IMAGE_DIR, image)
        save_image(content, image_name, OUTPUT_DIR)
