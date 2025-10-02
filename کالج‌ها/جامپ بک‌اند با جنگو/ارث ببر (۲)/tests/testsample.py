from pathlib import Path
from django.test import TestCase
from django.urls import reverse

from books.models import Book


class BookListTemplateTests(TestCase):
    fixtures = ("books.json", )

    @staticmethod
    def add_load_querystring_tag():
        template_path = Path(__file__).resolve().parent.parent / "books" / "templates" / "books" / "book_list.html"
        content = template_path.read_text(encoding="utf-8")
        content.replace('{% extends "base.html" %}', '{% extends "base.html" %}{% load querystring %}')
        content.replace("{% extends 'base.html' %}", "{% extends 'base.html' %}{% load querystring %}")
        template_path.write_text(content, encoding="utf-8")

    def setUp(self):
        self.add_load_querystring_tag()
        self.url = reverse("book_list")
        self.book = Book.objects.first()

    def test_template_inheritance(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "books/book_list.html")
        self.assertTemplateUsed(response, "base.html")

    def test_book_item_included(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "books/partials/book_item.html")

    
    def test_unknown_author(self):
        Book.objects.create(
            title="کتاب بدون نویسنده",
            author="",
            price=10000,
            publish_date="2023-05-20",
        )
        response = self.client.get(self.url)
        self.assertContains(response, "ناشناس")

    def test_empty_book_list_message(self):
        Book.objects.all().delete()
        response = self.client.get(self.url)
        self.assertContains(response, "هیچ کتابی یافت نشد.")