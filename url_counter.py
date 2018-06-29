import requests

from text_counter import count_text


def count_url(url):
    resp = requests.get(url)
    return count_text(resp.text)
