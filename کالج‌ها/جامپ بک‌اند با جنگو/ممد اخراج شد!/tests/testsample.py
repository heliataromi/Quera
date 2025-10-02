from pathlib import Path

from django.test import TestCase
from django.urls import reverse, resolve

from courses.models import Course


class TestSample(TestCase):
    def test_home_url_name(self):
        url = reverse('home')
        self.assertEqual(url, '/')
        resolver = resolve(url)
        self.assertEqual(resolver.view_name, 'home')

    def test_about_url_name(self):
        url = reverse('about')
        self.assertEqual(url, '/about/')
        resolver = resolve(url)
        self.assertEqual(resolver.view_name, 'about')

    def test_courses_list_url_name(self):
        url = reverse('courses:list')
        self.assertEqual(url, '/courses/')
        resolver = resolve(url)
        self.assertEqual(resolver.view_name, 'courses:list')

    def test_home_page_status_code_and_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_variables(self):
        template_path = Path('templates/home.html')
        content = template_path.read_text(encoding='utf-8')
        self.assertRegex(content, r'©\s*\{\{\s*year\s*\}\}\s*All rights reserved\.')

    def test_detail_page_contains_variables(self):
        course = Course.objects.create(
            title='دوره تست',
            price=100000,
            poster_url='https://example.com/image.png',
        )

        response = self.client.get(reverse('courses:detail', args=[course.pk]))
        content = response.content.decode()
        self.assertIn(course.poster_url, content)
        self.assertIn(course.title, content)

    def test_list_page_urls(self):
        template_path = Path('courses/templates/courses/list.html')
        content = template_path.read_text(encoding='utf-8')
        pattern = r'"\s*{%\s*url\s+\'home\'\s*%}"'
        self.assertRegex(content, pattern)