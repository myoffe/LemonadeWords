import requests

from text_counter import count_text


def count_url(url):
    resp = requests.get(url)
    resp.raise_for_status()
    return count_text(resp.text)
