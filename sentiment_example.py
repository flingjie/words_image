# -*- coding: utf-8 -*-
import os
from sentiment_analyser import get_words_sentiment
from words_image import show_emotion

BASE_DIR = os.path.dirname(__file__)
WEIBO_DIR = os.path.join(BASE_DIR, 'weibo')
WEIBO_PATH = os.path.join(WEIBO_DIR, 'happy.txt')


if __name__ == "__main__":
    words, sentiment = get_words_sentiment(WEIBO_PATH)
    show_emotion(words, sentiment)


