# -*- coding: utf-8 -*-
from words_image import generate_image
import os

base_dir = os.path.dirname(__file__)
words_dir = os.path.join(base_dir, "data")
image_name = os.path.join(base_dir, "nami.png")

if __name__ == "__main__":
    files = []
    for f in os.listdir(words_dir):
        full_f = os.path.join(words_dir, f)
        if os.path.isfile(full_f):
            files.append(full_f)
    generate_image(files, image_name)