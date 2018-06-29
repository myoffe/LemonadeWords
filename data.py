import os
import pickle
from collections import Counter

DATA_FILENAME = 'data.pickle'


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
