import types
import unittest
from main import divs


class TestSampleDivs(unittest.TestCase):

    def test_return_types(self):
        self.assertIsInstance(divs(10), types.GeneratorType, "خروجی کد شما از جنس generator نیست.")

    def test_number_10(self):
        ls = []
        for it in divs(10):
            ls.append(it)
        self.assertEqual([1, 2, 5, 10], ls,
                         'ورودی تابع عدد ۱۰ است و خروجی تابع که مقسوم‌علیه‌های عدد ۱۰ هستند باید [10, 5 ,2 ,1] باشد.')

    def test_number_1(self):
        ls = []
        for it in divs(1):
            ls.append(it)
        self.assertEqual([1], ls, 'ورودی تابع عدد ۱ است و خروجی تابع که مقسوم‌علیه‌های عدد ۱ هستند باید [1] باشد.')

    def test_number_6(self):
        ls = []
        for it in divs(6):
            ls.append(it)
        self.assertEqual([1, 2, 3, 6], ls,
                         'ورودی تابع عدد ۶ و خروجی تابع که مقسوم‌علیه‌های عدد ۶ هستند باید [6 ,3 ,2 ,1] باشد.')
