
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from gym.forms import SignUpForm
from gym.models import GymMember

class TestSampleTest(TestCase):
    def setUp(self):
        self.valid_data = {
            'email': 'test@example.com',
            'password': 'Password1',
            'password_confirm': 'Password1',
            'first_name': 'John',
            'last_name': 'Doe',
            'birthdate': (timezone.now().date().replace(year=timezone.now().year - 20)).isoformat(),
            'start_date': (timezone.now().date()).isoformat(),
        }
        self.signup_url = reverse('signup')
        self.form = SignUpForm()

    def test_valid_form(self):
        form = SignUpForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_duplicate_email(self):
        data = self.valid_data.copy()
        data.pop('password_confirm')
        GymMember.objects.create(**data)

        form = SignUpForm(data=self.valid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)
        self.assertEqual(
            form.errors.get('email')[0],  # type: ignore
            'This email is already registered. Please use a different email.'
        )

    def test_password_invalid(self):
        data = self.valid_data.copy()
        data['password'] = data['password_confirm'] = 'Short1'
        print(data)
        form = SignUpForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('password', form.errors)
        self.assertEqual(
            form.errors.get('password')[0],  # type: ignore
            'Password must be at least 8 characters long.'
        )

        data['password'] = data['password_confirm'] = 'password1'
        form = SignUpForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('password', form.errors)
        self.assertEqual(
            form.errors.get('password')[0],  # type: ignore
            'Password must contain at least one uppercase letter.'
        )

        data['password'] = data['password_confirm'] = 'Password'
        form = SignUpForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('password', form.errors)
        self.assertEqual(
            form.errors.get('password')[0],  # type: ignore
            'Password must contain at least one number.'
        )

    def test_passwords_do_not_match(self):
        data = self.valid_data.copy()
        data['password_confirm'] = 'DifferentPassword1'
        form = SignUpForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('__all__', form.errors)
        self.assertEqual(form.non_field_errors()[0], 'Passwords do not match.')

    def test_get_signup_view_renders_form(self):
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gym/signup.html')
        self.assertIn('form', response.context)

    def test_post_valid_signup_creates_member_and_redirects(self):
        response = self.client.post(self.signup_url, data=self.valid_data)
        self.assertEqual(GymMember.objects.count(), 1)
        member = GymMember.objects.first()
        self.assertRedirects(response, reverse('success', kwargs={'pk': member.id}))

    def test_post_invalid_signup_renders_form_with_errors(self):
        invalid_data = self.valid_data.copy()
        invalid_data['password_confirm'] = 'WrongPassword'
        response = self.client.post(self.signup_url, data=invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gym/signup.html')
        self.assertIn('form', response.context)
        self.assertTrue(response.context['form'].errors)
        self.assertEqual(GymMember.objects.count(), 0)