from flask import Flask, request

from data import read_data
from file_counter import count_file
from text_counter import count_text
from url_counter import count_url

app = Flask(__name__)


@app.route('/count', methods=['POST'])
def count():
    json = request.json
    if 'text' in json:
        return count_text(json['text'])
    elif 'file' in json:
        return count_file(json['file'])
    elif 'url' in json:
        return count_url(json['url'])
    else:
        return 'Expected one of: text, file, url'


@app.route('/stats/<word>', methods=['GET'])
def stats(word):
    freqs = read_data()
    return str(freqs.get(word))
