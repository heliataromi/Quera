from bs4 import BeautifulSoup


def process(name):
    with open(name) as fp:
        soup = BeautifulSoup(fp, 'html.parser')
        number_of_links = len(soup.find_all('a'))
        return number_of_links
