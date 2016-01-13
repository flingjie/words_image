# -*- coding: utf-8 -*-
from words_image import get_keywords, save_gif
import os

BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, "data")
GIF_DIR = os.path.join(BASE_DIR, "gifs")
GIF_PATH = os.path.join(GIF_DIR, "ace.gif")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")


if __name__ == "__main__":
    words = get_keywords(DATA_DIR)
    save_gif(words, GIF_PATH, OUTPUT_DIR)
