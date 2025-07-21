import unittest
from main import solve


class ScoreListTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual("10002 + 50 = 10052", solve("10# + 50 = 10052"),
                         'خروجی تابع به‌ازای ورودی 10052 = 50 + #10 باید 10052 = 50 + 10002 باشد.')

    def test_2(self):
        self.assertEqual("-1", solve("12 + 13 = #6"), 'خروجی تابع به‌ازای ورودی 6# = 13 + 12 باید 1- باشد.')

    def test_3(self):
        self.assertEqual("52979783 + 40838457 = 93818240", solve("52979783 + 40838457 = #40"),
                         'خروجی تابع به‌ازای ورودی 40# = 40838457 + 52979783 باید 93818240 = 40838457 + 52979783 باشد.')
