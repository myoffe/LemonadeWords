import re
from collections import Counter

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello Lemonade!"


@app.route('/count', methods=['POST'])
def count():
    text = request.json['text']
    words = get_words(text)
    freqs = Counter(words)
    return frequencies_string(freqs)


def frequencies_string(freqs):
    return '\n'.join([f'{word}: {times}' for word, times in freqs.items()])


def get_words(s):
    return re.sub('\W', ' ', s).lower().split()
