import os, sys, inspect
import time

from django.test import TestCase, Client
import requests
from ans import process
from qrequest.models import Book
import os

class TestBook(TestCase):

    def test_physic(self):
        os.system('python manage.py makemigrations&')
        os.system('python manage.py migrate&')
        os.system('python manage.py runserver &')
        time.sleep(10)
        proxies = {
            "http": None,
            "https": None,
        }
        book1 = Book(name='e', category='physic')
        book1.save()
        base_link = 'http://127.0.0.1:8000'
        endpoint = 'physic/'
        self.assertEqual('physic', process(base_link+'/'+endpoint), '\nچون category تمام کتاب‌های موجود در این مثال برابر physic است پس باید عبارت physic را بازگردانید.')
