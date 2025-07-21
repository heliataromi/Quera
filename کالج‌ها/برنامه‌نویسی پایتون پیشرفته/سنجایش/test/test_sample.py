import unittest

from main import decorator_builder


class ScoreListTest(unittest.TestCase):

    def test_sample_1(self):
        def validator(x):
            return x > 0

        @decorator_builder(validator)
        def f(x):
            return x

        self.assertEqual(f(10), 10,'\nتابع f فقط برای ورودی‌های بزرگتر از ۰ معتبر است. پس برای ورودی ۱۰، خروجی آن برابر ۱۰ خواهد بود.')
        self.assertEqual(f(-1), 'error', '\nتابع f فقط برای ورودی‌های بزرگتر از ۰ معتبر است. پس برای ورودی ۱- خروجی آن برابر error خواهد بود.')

    def test_sample_2(self):
        def validator(x, y):
            return type(x) == int and type(y) == int

        @decorator_builder(validator)
        def f(x, y):
            return x + y

        self.assertEqual(f(20, 10), 30, '\nتابع f جمع دو عدد را برمی‌گرداند. پس برای ورودی‌های ۲۰ و ۱۰، خروجی آن برابر ۳۰ خواهد بود.')
        self.assertEqual(f("34", 20), 'error', '\nتابع f جمع دو عدد را برمی‌گرداند. پس اگر یکی از ورودی‌های آن، رشته باشد؛ خروجی آن برابر error خواهد بود.')
