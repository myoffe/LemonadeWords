import os.path
import pickle
import re
from collections import Counter

from flask import Flask, request

DATA_FILENAME = 'data.pickle'

app = Flask(__name__)


@app.route('/count', methods=['POST'])
def count():
    json = request.json
    if 'text' in json:
        return count_string(json['text'])
    elif 'file' in json:
        return count_file(json['file'])
    else:
        return 'no inputs provided'


def count_string(input):
    words = get_words(input)
    freqs = Counter(words)
    update_data(freqs)
    return frequencies_string(freqs)


# TODO refactor a bit
def count_file(filename):
    with open(filename, 'r') as file:
        def read_chunk_full_words():
            data = file.read(1024)
            extra = ''
            new_char = file.read(1)
            while new_char.isalpha():
                extra += new_char
                new_char = file.read(1)

            return ''.join([data, extra])

        freqs = Counter()
        for chunk in iter(read_chunk_full_words, ''):
            words = get_words(chunk)
            freqs.update(Counter(words))

    update_data(freqs)
    return frequencies_string(freqs)


@app.route('/stats/<word>', methods=['GET'])
def stats(word):
    freqs = read_data()
    return str(freqs.get(word))


def frequencies_string(freqs):
    return '\n'.join([f'{word}: {times}' for word, times in freqs.items()])


def update_data(freqs):
    init_datafile_if_needed()
    with open_datafile_for_readwrite() as file:
        data = deserialize(file)
        data.update(freqs)
        serialize(data, file)


def read_data():
    init_datafile_if_needed()
    with open_datafile_for_read() as file:
        return deserialize(file)


def serialize(data, file):
    file.truncate()
    file.seek(0)
    pickle.dump(data, file, pickle.HIGHEST_PROTOCOL)  # I'm a pickle!


def deserialize(file):
    data = pickle.load(file)
    return data if type(data) == Counter else Counter()


def open_datafile_for_readwrite():
    return open(DATA_FILENAME, 'rb+')


def open_datafile_for_read():
    return open(DATA_FILENAME, 'rb')


def init_datafile_if_needed():
    if not os.path.isfile(DATA_FILENAME):
        with open(DATA_FILENAME, 'wb') as file:
            serialize(Counter(), file)


def get_words(s):
    return re.sub('\W', ' ', s).lower().split()
