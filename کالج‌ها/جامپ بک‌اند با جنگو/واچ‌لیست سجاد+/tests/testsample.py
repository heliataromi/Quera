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
        self.update_url = f'/api/update/6534/'
        self.edit_page_url = f'/6534/edit/'

    def test_update_view_url_is_correct(self):
        response = self.client.head(self.edit_page_url)
        self.assertEqual(response.status_code, 200)

    def test_update_api_url_is_correct(self):
        data = {'is_watched': True}
        response = self.client.patch(
            self.update_url,
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)

    def test_update_api_rejects_other_methods(self):
        response = self.client.get(self.update_url, data={})
        self.assertEqual(response.status_code, 405)
