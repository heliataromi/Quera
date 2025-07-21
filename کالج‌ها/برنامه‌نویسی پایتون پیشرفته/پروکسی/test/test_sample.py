import unittest

from main import Proxy


class Hi:
    def __init__(self):
        self.number = 0

    def f1(self):
        pass

    def f2(self):
        pass


class Test(unittest.TestCase):
    def test_sample_1(self):
        str_proxy = Proxy("test_string")
        self.assertTrue(isinstance(str_proxy, Proxy), 'نام کلاس مورد نظر باید Proxy باشد.')
        t = Hi()
        proxy = Proxy(t)
        proxy.number = 6
        self.assertTrue(6, t.number)

    def test_sample_2(self):
        proxy = Proxy("Test String")
        proxy.upper()
        self.assertEqual("upper", proxy.last_invoked_method())
        try:
            proxy.no_such_method()
            self.assertFalse(True)
        except Exception as e:
            self.assertEqual("No Such Method", str(e), 'تابع مورد نظر جزو توابع تعریف شده نیست؛ پس باید استثنایی با پیغام No Such Method پرتاب شود.')

        self.assertEqual(1, proxy.count_of_calls("upper"), 'متد upper تاکنون ۱ بار روی شئ مورد نظر فراخوانی شده است.')
        self.assertEqual(0, proxy.count_of_calls("capitalize"), 'متد ‌capitalize تاکنون روی شئ مورد نظر فراخوانی نشده است.')

    def test_sample_3(self):
        proxy = Proxy(Hi())
        proxy.f1()
        self.assertTrue(proxy.was_called("f1"), 'متد f1 روی شئ مورد نظر فراخوانی شده است.')
        self.assertFalse(proxy.was_called("f2"), 'متد f2 روی شئ مورد نظر فراخوانی نشده است.')
        proxy.f2()
        self.assertTrue(proxy.was_called("f2"), 'متد f2 روی شئ مورد نظر فراخوانی شده است.')
        self.assertFalse(proxy.was_called("not valid"), 'متد not valid روی شئ مورد نظر فراخوانی نشده است.')

    def test_sample_4(self):
        t = Hi()
        proxy = Proxy(t)

        try:
            proxy.last_invoked_method()
        except Exception as e:
            self.assertEqual("No Method Is Invoked", str(e), 'تا به حال متد معتبری فراخوانی نشده، پس باید استثنایی با پیغام No Method Is Invoked پرتاب شود.')

        proxy.f1()
        proxy.f2()
        self.assertEqual("f2", proxy.last_invoked_method(), 'آخرین متد معتبری که فراخوانی شده، f2 است.')
