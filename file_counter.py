from collections import Counter
from functools import partial

from data import update_data
from utils import get_words, frequencies_string

READ_CHUNK_SIZE = 10000


def count_file(filename):
    freqs = Counter()
    with open(filename, 'r') as file:
        chunk_reader = partial(_read_chunk_full_words, file)

        for chunk in iter(chunk_reader, ''):
            words = get_words(chunk)
            freqs.update(Counter(words))

    update_data(freqs)
    return frequencies_string(freqs)


def _read_chunk_full_words(file):
    data = file.read(READ_CHUNK_SIZE)
    extra = ''
    new_char = file.read(1)
    while new_char.isalpha():
        extra += new_char
        new_char = file.read(1)

    return ''.join([data, extra])
