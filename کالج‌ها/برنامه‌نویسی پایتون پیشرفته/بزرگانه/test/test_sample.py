import unittest

from main import capitalize


class Test(unittest.TestCase):

	def test_1(self):
		self.assertEqual(['Ali', 'Reyhaneh', 'Amir', 'Amir Abbas', 'Fatemeh Zahra'], capitalize(['ali', 'REYHANEH', 'aMIR', 'AMIR abbas', 'Fatemeh Zahra']), "\nبه ازای ورودی\n['ali', 'REYHANEH', 'aMIR', 'AMIR abbas', 'Fatemeh Zahra']\nخروجی تابع برابر\n['Ali', 'Reyhaneh', 'Amir', 'Amir Abbas', 'Fatemeh Zahra']\nاست.")

	def test_2(self):
		self.assertEqual(['Nazanin Zahra', 'Ali Gholi Khane Bozorg'], capitalize(['nazaNIN ZAHRA', 'ALI GHOLI KHANE bozorg']), "\nبه ازای ورودی\n['nazaNIN ZAHRA', 'ALI GHOLI KHANE bozorg']\nخروجی تابع برابر\n['Nazanin Zahra', 'Ali Gholi Khane Bozorg']\nاست.")