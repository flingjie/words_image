# -*- coding: utf-8 -*-
import jieba.analyse
from PIL import Image, ImageSequence
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import os
from images2gif import writeGif


MAX_WORDS = 1000
CUR_DIR = os.path.dirname(__file__)
SENTIMENT_DIR = os.path.join(CUR_DIR, "sentiment")
HAPPY_PATH = os.path.join(SENTIMENT_DIR, 'happy.png')
SAD_PATH = os.path.join(SENTIMENT_DIR, 'sad.png')
TEMP_DIR = os.path.join(CUR_DIR, 'tmp')


def get_keywords(data_dir):
    content = ''
    for f in os.listdir(data_dir):
        filename = os.path.join(data_dir, f)
        if os.path.isfile(filename):
            content += open(filename, 'rb').read()
            content += '\n'
    words = jieba.analyse.textrank(content, topK=MAX_WORDS, withWeight=True)
    return words


def generate_image(words, image):
    graph = np.array(image)
    wc = WordCloud(font_path=os.path.join(CUR_DIR, 'fonts/simhei.ttf'),
                   background_color='white', max_words=MAX_WORDS, mask=graph)
    wc.generate_from_frequencies(words)
    image_color = ImageColorGenerator(graph)
    return wc, image_color


def show_image(content, image_name):
    image = Image.open(image_name)
    wc, image_color = generate_image(content, image)
    plt.imshow(wc)
    plt.axis("off")
    plt.imshow(wc.recolor(color_func=image_color))
    plt.axis("off")
    plt.show()


def save_image(content, image_name, output_dir):
    image = Image.open(image_name)
    wc, image_color = generate_image(content, image)
    plt.imshow(wc)
    plt.axis("off")
    plt.imshow(wc.recolor(color_func=image_color))
    plt.axis("off")
    output_path = os.path.join(output_dir, os.path.basename(image_name))
    plt.savefig(output_path)


def show_emotion(content, sentiment):
    if sentiment < 0:
        image = Image.open(SAD_PATH)
    else:
        image = Image.open(HAPPY_PATH)
    wc, image_color = generate_image(content, image)
    plt.imshow(wc)
    plt.axis("off")
    plt.imshow(wc.recolor(color_func=image_color))
    plt.axis("off")
    plt.show()


def save_gif(content, gif_name, output_dir, duration=0.5):
    im = Image.open(gif_name)
    palette = im.getpalette()
    i = 0
    images = []
    try:
        while True:
            print("Start handle frame {}".format(i+1))
            im.putpalette(palette)
            new_im = Image.new('RGB', im.size, (255, 255, 255))
            new_im.paste(im)
            wc, image_color = generate_image(content, new_im)
            wc.recolor(color_func=image_color)
            images.append(wc.to_image())
            i += 1
            im.seek(im.tell() + 1)
    except EOFError:
        print("Process end")
    print("Start generate gif ... ")
    out_path = os.path.join(output_dir, os.path.basename(gif_name))
    writeGif(out_path, images, duration=duration)
