import unittest, math
from ..solution import Drug, Pharmacy


class DrugTest(unittest.TestCase):

    def setUp(self):
        self.drug1 = Drug("T1", 10, 1000)
        self.drug2 = Drug("T2", 20, 2000)
        self.drug3 = Drug("T3", 30, 3000)
        self.drug4 = Drug("T4", 40, 4000)
        self.store1 = Pharmacy("S1")
        self.store2 = Pharmacy("S2")

    def test_drug_constructor(self):
        self.assertEqual(self.drug1.name, "T1", '\nدر تابع سازنده کلاس Drug، نام دارو را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(self.drug1.amount, 10, '\nدر تابع سازنده کلاس Drug، مقدار دارو را به درستی مقداردهی نمی‌کنید.')
        self.assertEqual(self.drug1.price, 1000, '\nدر تابع سازنده کلاس Drug، قیمت دارو را به درستی مقداردهی نمی‌کنید.')

    def test_store_constructor(self):
        self.assertEqual(self.store1.name, "S1", '\nدر تابع سازنده کلاس Pharmacy، نام داروخانه را به درستی مقداردهی نمی‌کنید.')
        self.assertListEqual(self.store1.drugs, [], '\nدر تابع سازنده کلاس Pharmacy، لیست داروها در ابتدا برابر با یک لیست خالی می‌باشد.')
        self.assertListEqual(self.store1.employees, [], '\nدر تابع سازنده کلاس Pharmacy، لیست کارکنان در ابتدا برابر با یک لیست خالی می‌باشد.')

    def test_add_employee(self):
        self.assertListEqual(self.store1.employees, [], '\nکارمند مورد نظر را به درستی به لیست کارکنان اضافه نکرده‌اید.')

        self.store1.add_employee("Seyed Ali", "Babaei", 19)
        self.assertEqual(len(self.store1.employees), 1, '\nکارمند مورد نظر را به درستی به لیست کارکنان اضافه نکرده‌اید.')
        self.assertListEqual(self.store1.employees, [{'first_name': 'Seyed Ali', 'last_name': 'Babaei', 'age': 19}], '\nکارمند مورد نظر را به درستی به لیست کارکنان اضافه نکرده‌اید.')

    def test_store_value(self):
        self.store2.drugs.append(self.drug1)
        self.assertEqual(self.store2.total_value(), 10000, '\nقیمت تمام داروهای داروخانه برابر است با جمعِ حاصل‌ضرب مقدار هر دارو در قیمت آن.')
        self.store2.drugs.append(self.drug2)
        self.assertEqual(self.store2.total_value(), 50000, '\nقیمت تمام داروهای داروخانه برابر است با جمعِ حاصل‌ضرب مقدار هر دارو در قیمت آن.')
        self.store2.drugs.append(self.drug3)
        self.assertEqual(self.store2.total_value(), 140000, '\nقیمت تمام داروهای داروخانه برابر است با جمعِ حاصل‌ضرب مقدار هر دارو در قیمت آن.')
        self.store2.drugs.append(self.drug4)
        self.assertEqual(self.store2.total_value(), 300000, '\nقیمت تمام داروهای داروخانه برابر است با جمعِ حاصل‌ضرب مقدار هر دارو در قیمت آن.')
