import unittest
from ..function import sort_strings


class ScoreListTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_1(self):
        self.assertEqual(['Alireza', 'Arash', 'alireza', 'anahita', 'john', 'Maryam', 'Milad', 'Mohammad', 'sarah'],
                         sort_strings(['alireza', 'Mohammad', 'Arash', 'anahita', 'sarah', 'Milad', 'john', 'Alireza',
                                       'Maryam']), "\nبه ازای ورودی\n['alireza', 'Mohammad', 'Arash', 'anahita', 'sarah', 'Milad', 'john', 'Alireza','Maryam']\nخروجی تابع برابر\n['Alireza', 'Arash', 'alireza', 'anahita', 'john', 'Maryam', 'Milad', 'Mohammad', 'sarah']\nاست.")

    def test_2(self):
        self.assertEqual(['A', 'AA', 'AAA', 'Aa', 'a', 'aA', 'aa', 'aaa'],
                         sort_strings(['a', 'aa', 'aaa', 'A', 'AA', 'AAA', 'Aa', 'aA']), "\nبه ازای ورودی\n['a', 'aa', 'aaa', 'A', 'AA', 'AAA', 'Aa', 'aA']\nخروجی تابع برابر\n['A', 'AA', 'AAA', 'Aa', 'a', 'aA', 'aa', 'aaa']\nاست.")