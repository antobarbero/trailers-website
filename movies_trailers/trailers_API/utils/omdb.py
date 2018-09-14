import json

import requests

BASE_URL = 'http://www.omdbapi.com/'
API_KEY = '28e7ad89'


def get_movies(key_words):
    """Returns a list of movies that matches with the search words."""
    params = {
        'apikey': API_KEY,
        's': key_words
    }

    response = requests.get(BASE_URL, params=params)

    result = {}

    if response.ok:
        dict_response = json.loads(response.text)
        result = dict_response.get('Search', {})

    return result
