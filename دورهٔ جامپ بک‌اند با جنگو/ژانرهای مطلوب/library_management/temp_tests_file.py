from django.test import TestCase
from .models import Book


class TestAPI(TestCase):
    def setUp(self):
        Book.objects.create(title='A Thousand Splendid Suns', genre='Novel')
        Book.objects.create(title='Harry Potter and the Philosopher\'s Stone', genre='Fantasy')
        Book.objects.create(title='Harry Potter and the Chamber of Secrets', genre='Fantasy')

    def test_books(self):
        book_1 = Book.objects.get(title='A Thousand Splendid Suns')
        book_2 = Book.objects.get(title='Harry Potter and the Philosopher\'s Stone')
        book_3 = Book.objects.get(title='Harry Potter and the Chamber of Secrets')

        response = self.client.get('/books/Fantasy/')
        data = response.json()
        self.assertEqual(data.get('title'), 'List of Books')
        self.assertEqual(data.get('genre'), 'Fantasy')
        self.assertListEqual(data.get('books'), [book_2.id, book_3.id])

        response = self.client.get('/books/Novel/')
        data = response.json()
        self.assertEqual(data.get('title'), 'List of Books')
        self.assertEqual(data.get('genre'), 'Novel')
        self.assertListEqual(data.get('books'), [book_1.id])
