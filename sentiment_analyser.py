# -*- coding: utf-8 -*-
import os
import jieba

BASE_DIR = os.path.dirname(__file__)
TRAINING_DATA_DIR = os.path.join(BASE_DIR, 'BosonNLP_sentiment_score')
SENTIMENT_FILE = os.path.join(TRAINING_DATA_DIR, 'BosonNLP_sentiment_score.txt')
BASE_NUMBER = 8
WORDS_NUMBER = 100


def load_data():
    sentiment_data = {}
    with open(SENTIMENT_FILE, 'rb') as f:
        for line in f.readlines():
            if ' ' not in line:
                continue
            word, score = line.split(' ')
            sentiment_data[word.strip()] = float(score.strip())
    return sentiment_data


def get_words_sentiment(filename):
    sentiment_data = load_data()
    content = open(filename, 'rb').read()
    words = jieba.cut(content)
    sentiment = 0
    result = []
    for w in words:
        sentiment += sentiment_data.get(w, 0)
        result.append((w, int(sentiment + BASE_NUMBER)))
    factor = int(WORDS_NUMBER / len(result))
    result *= factor
    return result, sentiment


