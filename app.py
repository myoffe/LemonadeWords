from flask import Flask, request

from data import read_data
from file_counter import count_file
from text_counter import count_text
from url_counter import count_url
from xkcd_counter import count_xkcd

app = Flask(__name__)


@app.route('/count', methods=['POST'])
def count():
    json = request.json
    if len(json) == 0: return 'Expected one of: text, file, url, xkcd'

    counter_funcs = {
        'text': count_text,
        'file': count_file,
        'url': count_url,
        'xkcd': count_xkcd
    }

    key, value = next(iter(json.items()))
    return counter_funcs[key](value)


@app.route('/stats/<word>', methods=['GET'])
def stats(word):
    freqs = read_data()
    return str(freqs.get(word) or 0)
