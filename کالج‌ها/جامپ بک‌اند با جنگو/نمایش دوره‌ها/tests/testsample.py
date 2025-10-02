from django.test import TestCase

from courses.models import Course

class TestSamples(TestCase):
    def setUp(self):
        self.course = Course.objects.create(title='Course A', price=100000)
        Course.objects.create(title='Course B', price=200000)
        Course.objects.create(title='Course C', price=150000)

    def test_list_view_ordering_asc(self):
        response = self.client.get('/courses/?ordering=ASC')
        prices = [course.price for course in response.context['courses']]
        self.assertEqual(prices, sorted(prices))
        self.assertEqual(len(response.context['courses']), 3)
        self.assertEqual(response.context['ordering'], 'ASC')

    def test_detail_view_template(self):
        url = f'/courses/{self.course.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/course_detail.html')

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_template_used(self):
        response = self.client.get('/about/')
        self.assertTemplateUsed(response, 'about.html')
