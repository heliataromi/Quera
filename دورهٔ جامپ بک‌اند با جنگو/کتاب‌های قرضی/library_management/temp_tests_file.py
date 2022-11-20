from django.test import TestCase
import datetime

from .models import Member, Book, Borrowed


class MemberTest(TestCase):

    def setUp(self):
        member_1 = Member.objects.create(first_name='Helia', last_name='Taromi')
        member_2 = Member.objects.create(first_name='Armin', last_name='Nikkhah')
        book_1 = Book.objects.create(title='A Thousand Splendid Suns', genre='Novel')
        book_2 = Book.objects.create(title='Harry Potter and the Philosopher\'s Stone', genre='Fantasy')
        book_3 = Book.objects.create(title='Harry Potter and the Chamber of Secrets', genre='Fantasy')
        Borrowed.objects.create(member=member_1, book=book_1)
        Borrowed.objects.create(member=member_1, book=book_2)
        Borrowed.objects.create(member=member_2, book=book_3)

    def test_borrowed_books(self):
        member_1 = Member.objects.get(first_name='Helia')
        member_2 = Member.objects.get(first_name='Armin')
        book_1 = Book.objects.get(title='A Thousand Splendid Suns')
        book_2 = Book.objects.get(title='Harry Potter and the Philosopher\'s Stone')
        book_3 = Book.objects.get(title='Harry Potter and the Chamber of Secrets')
        self.assertEqual({book_2.id}, set(member_1.borrowed_books('Fantasy')))
        self.assertEqual({book_1.id}, set(member_1.borrowed_books('Novel')))
        self.assertEqual({book_3.id}, set(member_2.borrowed_books('Fantasy')))
