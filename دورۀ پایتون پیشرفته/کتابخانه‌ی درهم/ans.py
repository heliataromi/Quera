import requests


def process(url):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return 'Bad Query'
        data = response.json()
    except requests.exceptions.MissingSchema:
        return 'Bad Query'

    if len(data) == 0:
        return 'I can\'t recognize it'

    cat = data[0]['category']
    for book in data:
        if book['category'] != cat:
            return 'I can\'t recognize it'

    return cat
