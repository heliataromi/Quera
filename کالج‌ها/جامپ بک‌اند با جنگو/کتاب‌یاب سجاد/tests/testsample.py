from django.test import TestCase, Client

from store.models import Book


class BookFilterTest(TestCase):
    fixtures = ('books.json', )

    def test_all_blank_params(self):
        response = self.client.get('/books/?max_price=&min_price=&author=&title=')
        self.assertEqual(response.status_code, 200)
        
        books = response.context["books"]
        self.assertEqual(books.count(), 20)
        expected = Book.objects.all().order_by('-price')
        self.assertQuerySetEqual(books, expected)


    def test_all_params(self):
        response = self.client.get('/books/?title=grok&author=gurus&min_price=125000&max_price=138000')
        self.assertEqual(response.status_code, 200)
        
        books = response.context["books"]
        self.assertEqual(books.count(), 2)
        self.assertEqual(books[0].title, 'Grokking System Design Interview')
        self.assertEqual(books[1].title, 'Grokking the Coding Interview')
