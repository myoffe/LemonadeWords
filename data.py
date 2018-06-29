import os
import pickle
from collections import Counter

DATA_FILENAME = 'data.pickle'


def update_data(freqs):
    _init_datafile_if_needed()
    with _open_datafile_for_readwrite() as file:
        data = _deserialize(file)
        data.update(freqs)
        _serialize(data, file)


def read_data():
    _init_datafile_if_needed()
    with _open_datafile_for_read() as file:
        return _deserialize(file)


def _serialize(data, file):
    file.truncate()
    file.seek(0)
    pickle.dump(data, file, pickle.HIGHEST_PROTOCOL)  # I'm a pickle!


def _deserialize(file):
    data = pickle.load(file)
    return data if type(data) == Counter else Counter()


def _open_datafile_for_readwrite():
    return open(DATA_FILENAME, 'rb+')


def _open_datafile_for_read():
    return open(DATA_FILENAME, 'rb')


def _init_datafile_if_needed():
    if not os.path.isfile(DATA_FILENAME):
        with open(DATA_FILENAME, 'wb') as file:
            _serialize(Counter(), file)
