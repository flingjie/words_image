# -*- coding: utf-8 -*-
import jieba.analyse
from PIL import Image, ImageFont
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import os


MAX_WORDS = 1000
CUR_DIR = os.path.dirname(__file__)


def get_keywords(data_dir):
    content = ''
    for f in os.listdir(data_dir):
        filename = os.path.join(data_dir, f)
        if os.path.isfile(filename):
            content += open(filename, 'rb').read()
            content += '\n'
    words = jieba.analyse.textrank(content, topK=MAX_WORDS, withWeight=True)
    return words


def generate_image(words, src_image):
    graph = np.array(Image.open(src_image))
    wc = WordCloud(font_path=os.path.join(CUR_DIR, 'fonts/simhei.ttf'),
                   background_color='white', max_words=MAX_WORDS, mask=graph)
    wc.generate_from_frequencies(words)
    image_color = ImageColorGenerator(graph)
    return wc, image_color


def show_image(content, image_name):
    wc, image_color = generate_image(content, image_name)
    plt.imshow(wc)
    plt.axis("off")
    plt.imshow(wc.recolor(color_func=image_color))
    plt.axis("off")
    plt.show()


def save_image(content, image_name, output_dir):
    wc, image_color = generate_image(content, image_name)
    plt.imshow(wc)
    plt.axis("off")
    plt.imshow(wc.recolor(color_func=image_color))
    plt.axis("off")
    output_path = os.path.join(output_dir, os.path.basename(image_name))
    plt.savefig(output_path)