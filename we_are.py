from words_image import generate_image
import os

base_dir = os.path.dirname(__file__)
filename = os.path.join(base_dir, "we_are.txt")
image_name = os.path.join(base_dir, "we_are.png")

if __name__ == "__main__":
    generate_image(filename, image_name)