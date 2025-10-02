import requests


def add_book(book: dict[str, str]) -> str or None:
    urls = {
        'mathematics': 'http://127.0.0.1:8000/mathematics/',
        'physics': 'http://127.0.0.1:8000/physics/',
        'chess': 'http://127.0.0.1:8000/chess/'
    }

    category = book['category']
    url = urls.get(category)

    if url is None:
        return "Invalid Category"

    response = requests.get(url)

    if response.status_code == 200:
        books_list = response.json()

        for existing_book in books_list:
            if existing_book['name'] == book['name']:
                return "Bad Request"

        requests.post(url, json=book)
    else:
        return "Bad Request"

