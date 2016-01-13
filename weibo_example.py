# -*- coding: utf-8 -*-
import os
from sentiment_analyser import get_words_sentiment
from words_image import show_emotion

BASE_DIR = os.path.dirname(__file__)
WEIBO_DIR = os.path.join(BASE_DIR, 'weibo')
WEIBO_PATH = os.path.join(WEIBO_DIR, 'happy.txt')
IMAGE_DIR = os.path.join(BASE_DIR, "images")
HAPPY_PATH = os.path.join(IMAGE_DIR, 'happy.png')
SAD_PATH = os.path.join(IMAGE_DIR, 'sad.png')

if __name__ == "__main__":
    words, sentiment = get_words_sentiment(WEIBO_PATH)
    show_emotion(words, sentiment)


