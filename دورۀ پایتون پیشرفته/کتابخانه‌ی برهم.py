import requests


def process(book):
    book_category = book['category']
    url = 'http://127.0.0.1:8000/' + book_category + '/'
    category = requests.get(url).json()
    names = [b['name'] for b in category]
    if book['name'] in names:
        return 'Bad Query'
    requests.post(url, book)
