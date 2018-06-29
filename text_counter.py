from collections import Counter

from data import update_data
from utils import frequencies_string, get_words


def count_text(input):
    words = get_words(input)
    freqs = Counter(words)
    update_data(freqs)
    return frequencies_string(freqs)
