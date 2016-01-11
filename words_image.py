# -*- coding: utf-8 -*-
import jieba.analyse
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import os


MAX_WORDS = 1000
CUR_DIR = os.path.dirname(__file__)


def process_text(content):
    words = jieba.analyse.textrank(content, topK=MAX_WORDS, withWeight=True)
    return words


def get_content(files):
    content = ''
    for f in files:
        content += open(f, 'rb').read()
        content += '\n'
    return content


def generate_image(files, src_image):
    content = get_content(files)
    graph = np.array(Image.open(src_image))
    wc = WordCloud(font_path=os.path.join(CUR_DIR, 'fonts/simhei.ttf'),
                   background_color='white', max_words=MAX_WORDS, mask=graph)
    words = process_text(content)
    wc.generate_from_frequencies(words)
    image_color = ImageColorGenerator(graph)
    return wc, image_color


def show_image(files, image_name):
    wc, image_color = generate_image(files, image_name)
    plt.imshow(wc)
    plt.axis("off")
    plt.imshow(wc.recolor(color_func=image_color))
    plt.axis("off")
    plt.show()


def save_image(files, image_name):
    wc, image_color = generate_image(files, image_name)
    plt.imshow(wc)
    plt.axis("off")
    plt.imshow(wc.recolor(color_func=image_color))
    plt.axis("off")
    plt.savefig("result_" + os.path.basename(image_name))