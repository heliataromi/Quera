import unittest

from main import real_numbers


class ScoreListTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_1(self):
        self.assertListEqual(['LEGAL', 'ILLEGAL'], real_numbers(['1.0', '1.']), "\nبه‌ازای ورودی ['1.0', '1.'] خروجی تابع برابر ['LEGAL', 'ILLEGAL'] است.")

    def test_2(self):
        self.assertListEqual(['LEGAL', 'ILLEGAL'], real_numbers(['1E000000000000000004', '1.']), "\nبه‌ازای ورودی ['1E000000000000000004', '1.'] خروجی تابع برابر ['LEGAL', 'ILLEGAL'] است.")

    def test_3(self):
        self.assertListEqual(['LEGAL', 'LEGAL', 'LEGAL', 'ILLEGAL'],
                             real_numbers(['1.0', '1e0', '1E000000000000000004', '1.']), "\nبه‌ازای ورودی ['1.0', '1e0', '1E000000000000000004', '1.'] خروجی تابع برابر ['LEGAL', 'LEGAL', 'LEGAL', 'ILLEGAL'] است.")
