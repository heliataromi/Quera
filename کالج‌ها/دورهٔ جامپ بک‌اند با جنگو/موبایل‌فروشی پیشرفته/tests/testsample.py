from django.test import TestCase

from mobilestore import queries
from mobilestore.models import Brand


class TestTasks(TestCase):
    fixtures = ('store',)

    def test_all_brands_not_in_korea_china(self):
        solution = Brand.objects.filter(id__in=[4])
        answer = queries.all_brands_not_in_korea_china()
        self.assertQuerysetEqual(
            solution, answer, ordered=False, transform=lambda x: x,
            msg='\nتابع all_brands_not_in_korea_china با استفاده از تابع filter و آبجکت Q، باید برندهایی که ملیت آن‌ها China یا Korea نیست را بازگرداند.'
        )