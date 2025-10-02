from django import forms
from django.test import TestCase

from bmi.forms import BMIForm


class TestSampleTest(TestCase):
    def test_fields_exist(self):
        form = BMIForm()
        fields = list(form.fields.keys())
        self.assertIn('height', fields)
        self.assertIn('weight', fields)
        self.assertIn('age', fields)
        self.assertIn('gender', fields)

    def test_valid_form(self):
        data = {
            "height": 180,
            "weight": 75,
            "age": 25,
            "gender": "M"
        }
        form = BMIForm(data=data)
        self.assertTrue(form.is_valid())

        result = form.get_result()
        self.assertIn("bmi", result)
        self.assertIn("category", result)
        self.assertIn("body_fat", result)

    def test_missing_fields(self):
        data = {
            "height": 180,
            "weight": 75,
        }
        form = BMIForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('age', form.errors)
        self.assertIn('gender', form.errors)

    def test_invalid_values(self):
        data = {
            "height": -10,
            "weight": 0,
            "age": 150,
            "gender": "X"
        }
        form = BMIForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('height', form.errors)
        self.assertIn('weight', form.errors)
        self.assertIn('age', form.errors)
        self.assertIn('gender', form.errors)
