from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from gym.forms import CourseForm, EnrollmentForm
from gym.models import Course, Enrollment


class CourseFormTests(TestCase):
    def setUp(self):
        self.valid_data = {
            'name': 'Crossfit',
            'coach': 'GholamReza',
            'start_date': timezone.now().date() + timezone.timedelta(days=10),
            'end_date': timezone.now().date() + timezone.timedelta(days=100),
            'capacity': 45,
        }

    def test_course_form(self):
        form = CourseForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

        data = self.valid_data.copy()
        data['capacity'] = 1
        form = CourseForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('capacity', form.errors)
        self.assertEqual('Capacity should be at least 5.', form.errors['capacity'][0])

        data = self.valid_data.copy()
        data['start_date'] = (timezone.now().date() - timezone.timedelta(days=10))
        form = CourseForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('start_date', form.errors)
        self.assertEqual('Start date cannot be in the past.', form.errors['start_date'][0])

        data = self.valid_data.copy()
        data['end_date'] = data['start_date']
        form = CourseForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('End date must be after start date.', form.non_field_errors())

    def test_course_form_widgets_and_fields(self):
        form = CourseForm()
        self.assertEqual(form.fields['name'].widget.attrs.get('class'), 'form-control')
        self.assertEqual(form.fields['coach'].widget.attrs.get('class'), 'form-control')
        self.assertEqual(form.fields['start_date'].widget.attrs.get('class'), 'form-control')
        self.assertEqual(form.fields['end_date'].widget.attrs.get('class'), 'form-control')
        self.assertEqual(form.fields['capacity'].widget.attrs.get('class'), 'form-control')
        self.assertEqual(form.fields['start_date'].widget.input_type, 'date')
        self.assertEqual(form.fields['end_date'].widget.input_type, 'date')
        self.assertListEqual(sorted(form.fields.keys()), ['capacity', 'coach', 'end_date', 'name', 'start_date'])


class EnrollmentFormTests(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            name='Crossfit',
            coach='GholamReza',
            start_date=timezone.now().date() + timezone.timedelta(days=10),
            end_date=timezone.now().date() + timezone.timedelta(days=100),
            capacity=2
        )
        self.valid_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'national_id': '1234567890',
            'email': 'john@example.com',
        }

    def test_enrollment_form(self):
        form = EnrollmentForm(data=self.valid_data, course=self.course)
        self.assertTrue(form.is_valid())

        Enrollment.objects.create(course=self.course, first_name='Gholam', last_name='Gholami', national_id='0123456789', email='gholam@gg.com')
        Enrollment.objects.create(course=self.course, first_name='Reza', last_name='Rezaie', national_id='1234567890', email='reza@gg.com')
        form = EnrollmentForm(data=self.valid_data, course=self.course)
        self.assertFalse(form.is_valid())
        self.assertIn('This course is already full.', form.non_field_errors())

    def test_enrollment_form_widgets_and_fields(self):
        form = EnrollmentForm()
        self.assertEqual(form.fields['first_name'].widget.attrs.get('class'), 'form-control')
        self.assertEqual(form.fields['last_name'].widget.attrs.get('class'), 'form-control')
        self.assertEqual(form.fields['national_id'].widget.attrs.get('class'), 'form-control')
        self.assertEqual(form.fields['email'].widget.attrs.get('class'), 'form-control')
        self.assertListEqual(sorted(form.fields.keys()), ['email', 'first_name', 'last_name', 'national_id'])


class CreateCourseViewTests(TestCase):
    def setUp(self):
        self.url = reverse('create_course')
        self.valid_data = {
            'name': 'Yoga',
            'coach': 'Alice',
            'start_date': timezone.now().date(),
            'end_date': timezone.now().date() + timezone.timedelta(days=10),
            'capacity': 10,
        }

    def test_get_create_course_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gym/create_course.html')
        self.assertIn('form', response.context)

        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(Course.objects.count(), 1)
        self.assertRedirects(response, reverse('home'))


class EnrollViewTests(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            name='Yoga',
            coach='Alice',
            start_date=timezone.now().date(),
            end_date=timezone.now().date() + timezone.timedelta(days=10),
            capacity=2
        )
        self.url = reverse('enroll', args=[self.course.id])
        self.valid_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'national_id': '1234567890',
            'email': 'john@example.com',
        }

    def test_get_enroll_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gym/enroll.html')
        self.assertIn('form', response.context)
        self.assertIn('course', response.context)

        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(Enrollment.objects.count(), 1)
        self.assertRedirects(response, reverse('home'))
