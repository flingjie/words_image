import jieba.analyse
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator


MAX_WORDS = 1000

def process_text(content):
    result = jieba.analyse.textrank(content, topK=MAX_WORDS, withWeight=True)
    min_weight = result[-1][1]
    words = []
    for word,weight in result:
        n = int(weight/min_weight)
        words.append((word, n))
    return words

def generate_image(filename, image_name):
    content = open(filename, 'rb').read()
    graph = np.array(Image.open(image_name))
    wc = WordCloud(background_color='white', max_words=MAX_WORDS, mask=graph)
    words = process_text(content)
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
