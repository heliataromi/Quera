import unittest
import requests_mock

from main import find_category


class TestFindCategory(unittest.TestCase):

    BASE_URL = 'http://127.0.0.1:8000'

    # --- Success tests for the 'physics' category ---

    @requests_mock.Mocker()
    def test_physics_with_single_book(self, m):
        """Tests successful recognition for 'physics' with a single book in the response."""
        category = 'physics'
        url = f'{self.BASE_URL}/{category}'
        mock_data = [{'name': 'A Brief History of Time', 'category': category}]
        m.get(url, json=mock_data, status_code=200)

        expected = category
        actual = find_category(url)
        self.assertEqual(actual, expected, f"برای دسته‌بندی '{category}' با یک کتاب، نتیجه باید '{expected}' باشد.")


    # --- Tests for failure and edge cases ---

    @requests_mock.Mocker()
    def test_mixed_categories(self, m):
        """Tests for 'I can't recognize it' when the response contains mixed categories."""
        url = f'{self.BASE_URL}/mixed'
        mock_data = [
            {'name': 'Physics Book', 'category': 'physics'},
            {'name': 'Math Book', 'category': 'mathematics'}
        ]
        m.get(url, json=mock_data, status_code=200)

        expected = "I can't recognize it"
        actual = find_category(url)
        self.assertEqual(actual, expected, "در صورت وجود دسته‌بندی‌های مختلف، باید پیام عدم تشخیص برگردانده شود.")
