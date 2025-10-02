import unittest
import requests_mock

from main import add_book


class TestAddBook(unittest.TestCase):

    def setUp(self):
        """Set up common variables for the tests."""
        self.base_url = "http://127.0.0.1:8000"

    @requests_mock.Mocker()
    def test_add_new_mathematics_book_successfully(self, m):
        """Tests adding a new book to the 'mathematics' category."""
        category = 'mathematics'
        url = f"{self.base_url}/{category}/"
        book_data = {'name': 'Calculus 101', 'category': category}
        m.get(url, json=[])
        post_mock = m.post(url)

        result = add_book(book_data)

        self.assertIsNone(result)
        self.assertTrue(post_mock.called_once)
        self.assertEqual(post_mock.last_request.json(), book_data)

    @requests_mock.Mocker()
    def test_add_existing_physics_book_fails(self, m):
        """Tests that adding an existing physics book returns 'Bad Request'."""
        category = 'physics'
        url = f"{self.base_url}/{category}/"
        existing_book = {'name': 'Quantum Mechanics', 'category': category}
        m.get(url, json=[existing_book])
        post_mock = m.post(url)

        result = add_book(existing_book)

        self.assertEqual(result, "Bad Request")
        self.assertFalse(post_mock.called)
