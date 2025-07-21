import unittest

from main import calculator


class Test(unittest.TestCase):

	def test_1(self):
		n = 10
		m = 1
		li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
		self.assertEqual(-5, calculator(n, m, li), '\nبه ازای\nn=10 و m=1 و li=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\nخروجی تابع برابر 5- است.')