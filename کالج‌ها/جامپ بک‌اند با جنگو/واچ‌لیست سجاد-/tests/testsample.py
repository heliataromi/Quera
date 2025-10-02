from django.test import TestCase, Client
from watchlist.models import WatchItem

import json

class ViewsTestSample(TestCase):
    def setUp(self):
        self.client = Client()
        self.item = WatchItem.objects.create(
            id=6534,
            title='Inception',
            type='M',
            url='https://example.com/inception',
            is_watched=False,
        )
        self.delete_api_url = f'/api/delete/6534/'
        self.delete_view_url = f'/6534/delete/'

    def test_delete_view_url_is_correct(self):
        response = self.client.get(self.delete_view_url)
        self.assertNotEqual(response.status_code, 404)

    def test_delete_api_url_is_correct(self):
        response = self.client.get(self.delete_view_url)
        self.assertNotEqual(response.status_code, 404)

    def test_delete_api_rejects_other_methods(self):
        for method in ['get', 'post', 'put', 'patch']:
            response = getattr(self.client, method)(self.delete_api_url)
            self.assertEqual(response.status_code, 405)
