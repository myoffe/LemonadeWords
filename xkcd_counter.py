import requests

from text_counter import count_text


def count_xkcd(comic_number):
    resp = requests.get(f'https://xkcd.com/{comic_number}/info.0.json')
    resp.raise_for_status()
    return count_text(resp.json()['transcript'])
