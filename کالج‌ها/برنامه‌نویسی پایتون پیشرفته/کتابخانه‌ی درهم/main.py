import requests


def find_category(url: str) -> str:
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return 'Bad Request'

        data = response.json()
    except:
        return 'Bad Request'

    if len(data) == 0:
        return 'I can\'t recognize it'

    category = data[0]['category']
    if not all(category == book['category'] for book in data):
        return 'I can\'t recognize it'

    return category

