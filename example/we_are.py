from __future__ import absolute_import
from words_image import generate_image
import os

base_dir = os.path.dirname(__file__)
filename = os.path.join(base_dir, "data/we_are.txt")
image_name = os.path.join(base_dir, "data/aa.png")

if __name__ == "__main__":
    generate_image(filename, image_name)