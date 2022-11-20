from django.test import TestCase
import datetime

from .models import Book, Author


class AuthorTests(TestCase):
    def setUp(self):
        self.author_1 = Author.objects.create(first_name='Joanne Kathleen',
                                              last_name='Rowling',
                                              date_of_birth=datetime.date(1965, 7, 31))
        self.author_2 = Author.objects.create(first_name='John Ronald Reuel',
                                              last_name='Tolkien',
                                              date_of_birth=datetime.date(1892, 1, 3),
                                              date_of_death=datetime.date(1973, 9, 2))

    def test_is_alive(self):
        self.assertTrue(self.author_1.is_alive())
        self.assertFalse(self.author_2.is_alive())

    def test_get_age(self):
        self.assertEqual(datetime.date.today() - datetime.date(1965, 7, 31), self.author_1.get_age())
        self.assertEqual(datetime.date(1973, 9, 2) - datetime.date(1892, 1, 3), self.author_2.get_age())

    def test_str(self):
        self.assertEqual('Joanne Kathleen Rowling', self.author_1.__str__())
        self.assertEqual('John Ronald Reuel Tolkien', self.author_2.__str__())


class BookTests(TestCase):
    def setUp(self):
        self.author_1 = Author.objects.create(first_name='Joanne Kathleen',
                                              last_name='Rowling',
                                              date_of_birth=datetime.date(1965, 7, 31))
        self.author_2 = Author.objects.create(first_name='John Ronald Reuel',
                                              last_name='Tolkien',
                                              date_of_birth=datetime.date(1892, 1, 3),
                                              date_of_death=datetime.date(1973, 9, 2))
        self.book_1 = Book.objects.create(title='Harry Potter and the Philosopher\'s Stone',
                                          author=self.author_1,
                                          date_of_publish=datetime.date(1997, 6, 26))
        self.book_2 = Book.objects.create(title='Harry Potter and the Chamber of Secrets',
                                          author=self.author_1,
                                          date_of_publish=datetime.date(1998, 7, 2))
        self.book_3 = Book.objects.create(title='The Ring Sets Out',
                                          author=self.author_2,
                                          date_of_publish=datetime.date(1954, 7, 29))

    def test_get_age(self):
        self.assertEqual(self.book_1.get_age(), datetime.date.today() - datetime.date(1997, 6, 26))
        self.assertEqual(self.book_2.get_age(), datetime.date.today() - datetime.date(1998, 7, 2))
        self.assertEqual(self.book_3.get_age(), datetime.date.today() - datetime.date(1954, 7, 29))

    def test_str(self):
        self.assertEqual(self.book_1.__str__(), 'Harry Potter and the Philosopher\'s Stone',)
        self.assertEqual(self.book_2.__str__(), 'Harry Potter and the Chamber of Secrets')
        self.assertEqual(self.book_3.__str__(), 'The Ring Sets Out')


class ViewTests(TestCase):
    def setUp(self):
        self.author_1 = Author.objects.create(first_name='Joanne Kathleen',
                                              last_name='Rowling',
                                              date_of_birth=datetime.date(1965, 7, 31))
        self.author_2 = Author.objects.create(first_name='John Ronald Reuel',
                                              last_name='Tolkien',
                                              date_of_birth=datetime.date(1892, 1, 3),
                                              date_of_death=datetime.date(1973, 9, 2))
        self.book_1 = Book.objects.create(title='Harry Potter and the Philosopher\'s Stone',
                                          author=self.author_1,
                                          date_of_publish=datetime.date(1997, 6, 26))
        self.book_2 = Book.objects.create(title='Harry Potter and the Chamber of Secrets',
                                          author=self.author_1,
                                          date_of_publish=datetime.date(1998, 7, 2))
        self.book_3 = Book.objects.create(title='The Ring Sets Out',
                                          author=self.author_2,
                                          date_of_publish=datetime.date(1954, 7, 29))

    def test_booklist(self):
        response = self.client.get('/booklist/60/25/')
        self.assertContains(response, self.book_2)
        self.assertContains(response, self.book_3)
