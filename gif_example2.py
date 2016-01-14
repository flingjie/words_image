# -*- coding: utf-8 -*-
from words_image import get_keywords, words2gif_from_images
import os

BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, "data")
GIF_DIR = os.path.join(BASE_DIR, "gifs")
IMAGE_PATH = os.path.join(GIF_DIR, "one_piece")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")


if __name__ == "__main__":
    words = get_keywords(DATA_DIR)
    words2gif_from_images(words, IMAGE_PATH, OUTPUT_DIR)
