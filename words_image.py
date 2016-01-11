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


def generate_image(files, image_name):
    content = ''
    for f in files:
        content += open(f, 'rb').read()
        content += '\n'
    graph = np.array(Image.open(image_name))
    wc = WordCloud(font_path=os.path.join(CUR_DIR, 'fonts/simhei.ttf'),
                   background_color='white', max_words=MAX_WORDS, mask=graph)
    words = process_text(content)
    print(len(words))
    wc.generate_from_frequencies(words)
    image = ImageColorGenerator(graph)

    plt.imshow(wc)
    plt.axis("off")
    plt.imshow(wc.recolor(color_func=image))
    plt.axis("off")
    plt.figure()
    plt.imshow(graph, cmap=plt.cm.gray)
    plt.axis("off")
    plt.show()
