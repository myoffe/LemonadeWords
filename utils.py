import re


def frequencies_string(freqs):
    return '\n'.join([f'{word}: {times}' for word, times in freqs.items()])


def get_words(chunk):
    return re.sub('[^a-zA-Z]', ' ', chunk).lower().split()
