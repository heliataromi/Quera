import unittest, types
from main import ExceptionProxy, transform_exceptions


class ScoreListTest(unittest.TestCase):

    def test_normal(self):
        def f():
            1 / 0

        def g():
            int("salam")

        def h():
            "salam" + 1

        func_ls = [f, g, h]
        user_ls = transform_exceptions(func_ls)
        self.assertEqual(len(user_ls), 3, '\nتابع transform_exceptions باید به ازای هر ورودی، یک پیغام داشته باشد.')

        self.assertEqual(True, isinstance(user_ls[0], ExceptionProxy), '\nخروجی تابع transform_exceptions باید شئ‌ای از کلاس ExceptionProxy باشد.')
        self.assertEqual(user_ls[0].message, "division by zero", '\nدر صورتی که مخرج کسر برابر ۰ بود، باید پیغام خطا برابر با division by zero باشد.')
        self.assertEqual(user_ls[0].function.__name__, "f", '\nدر تابع f، خطای تقسیم بر ۰ اتفاق می‌افتد.')

        self.assertEqual(True, isinstance(user_ls[1], ExceptionProxy), '\nخروجی تابع transform_exceptions باید شئ‌ای از کلاس ExceptionProxy باشد.')
        self.assertEqual(user_ls[1].message, "invalid literal for int() with base 10: 'salam'", "\nهنگامی که در حال تبدیل رشته‌ی 'salam' به عدد بودیم، باید پیغام خطا برابر با invalid literal for int() with base 10: 'salam' باشد.")
        self.assertEqual(user_ls[1].function.__name__, "g", "\nدر تابع g، خطای عدم تبدیل رشته‌ی 'salam' به عدد اتفاق می‌افتد.")

        self.assertEqual(True, isinstance(user_ls[2], ExceptionProxy), '\nخروجی تابع transform_exceptions باید شئ‌ای از کلاس ExceptionProxy باشد.')
        self.assertEqual(user_ls[2].message, 'can only concatenate str (not "int") to str', '\nدر صورتی که در حال جمع یک عدد با یک رشته بودیم، باید پیغام خطا برابر با can only concatenate str (not "int") to str باشد.')
        self.assertEqual(user_ls[2].function.__name__, "h", '\nدر تابع h، خطای جمع یک عدد با یک رشته اتفاق می‌افتد.')

    def test_raised_exception(self):
        def f():
            raise NameError('salam')

        def g():
            raise ValueError

        def h():
            raise ZeroDivisionError

        func_ls = [f, g, f, f, g, h, f, h, g, g, h]
        user_ls = transform_exceptions(func_ls)

        self.assertEqual(len(user_ls), 11)
        self.assertEqual(True, isinstance(user_ls[0], ExceptionProxy), '\nخروجی تابع transform_exceptions باید شئ‌ای از کلاس ExceptionProxy باشد.')
        self.assertEqual(user_ls[0].message, "salam", '\nپیغام خطای مورد نظر برابر salam است.')
        self.assertEqual(user_ls[0].function.__name__, "f", '\nخطای مورد نظر در تابع f اتفاق می‌افتد.')

        self.assertEqual(True, isinstance(user_ls[1], ExceptionProxy), '\nخروجی تابع transform_exceptions باید شئ‌ای از کلاس ExceptionProxy باشد.')
        self.assertEqual(user_ls[1].message, "", '\nخطای مورد نظر پیغامی ندارد.')
        self.assertEqual(user_ls[1].function.__name__, "g", '\nخطای مورد نظر در تابع g اتفاق می‌افتد.')

        self.assertEqual(True, isinstance(user_ls[2], ExceptionProxy), '\nخروجی تابع transform_exceptions باید شئ‌ای از کلاس ExceptionProxy باشد.')
        self.assertEqual(user_ls[2].message, "salam", '\nپیغام خطای مورد نظر برابر salam است.')
        self.assertEqual(user_ls[2].function.__name__, "f", '\nخطای مورد نظر در تابع f اتفاق می‌افتد.')

        self.assertEqual(True, isinstance(user_ls[3], ExceptionProxy), '\nخروجی تابع transform_exceptions باید شئ‌ای از کلاس ExceptionProxy باشد.')
        self.assertEqual(user_ls[3].message, "salam", '\nپیغام خطای مورد نظر برابر salam است.')
        self.assertEqual(user_ls[3].function.__name__, "f", '\nخطای مورد نظر در تابع f اتفاق می‌افتد.')

        self.assertEqual(True, isinstance(user_ls[4], ExceptionProxy), '\nخروجی تابع transform_exceptions باید شئ‌ای از کلاس ExceptionProxy باشد.')
        self.assertEqual(user_ls[4].message, "", '\nخطای مورد نظر پیغامی ندارد.')
        self.assertEqual(user_ls[4].function.__name__, "g", '\nخطای مورد نظر در تابع g اتفاق می‌افتد.')

        self.assertEqual(True, isinstance(user_ls[5], ExceptionProxy), '\nخروجی تابع transform_exceptions باید شئ‌ای از کلاس ExceptionProxy باشد.')
        self.assertEqual(user_ls[5].message, "", '\nخطای مورد نظر پیغامی ندارد.')
        self.assertEqual(user_ls[5].function.__name__, "h", '\nخطای مورد نظر در تابع h اتفاق می‌افتد.')

        self.assertEqual(True, isinstance(user_ls[6], ExceptionProxy), '\nخروجی تابع transform_exceptions باید شئ‌ای از کلاس ExceptionProxy باشد.')
        self.assertEqual(user_ls[6].message, "salam", '\nپیغام خطای مورد نظر برابر salam است.')
        self.assertEqual(user_ls[6].function.__name__, "f", '\nخطای مورد نظر در تابع f اتفاق می‌افتد.')

        self.assertEqual(True, isinstance(user_ls[7], ExceptionProxy), '\nخروجی تابع transform_exceptions باید شئ‌ای از کلاس ExceptionProxy باشد.')
        self.assertEqual(user_ls[7].message, "", '\nخطای مورد نظر پیغامی ندارد.')
        self.assertEqual(user_ls[7].function.__name__, "h", '\nخطای مورد نظر در تابع h اتفاق می‌افتد.')

        self.assertEqual(True, isinstance(user_ls[8], ExceptionProxy), '\nخروجی تابع transform_exceptions باید شئ‌ای از کلاس ExceptionProxy باشد.')
        self.assertEqual(user_ls[8].message, "", '\nخطای مورد نظر پیغامی ندارد.')
        self.assertEqual(user_ls[8].function.__name__, "g", '\nخطای مورد نظر در تابع g اتفاق می‌افتد.')

        self.assertEqual(True, isinstance(user_ls[9], ExceptionProxy), '\nخروجی تابع transform_exceptions باید شئ‌ای از کلاس ExceptionProxy باشد.')
        self.assertEqual(user_ls[9].message, "", '\nخطای مورد نظر پیغامی ندارد.')
        self.assertEqual(user_ls[9].function.__name__, "g", '\nخطای مورد نظر در تابع g اتفاق می‌افتد.')

        self.assertEqual(True, isinstance(user_ls[10], ExceptionProxy), '\nخروجی تابع transform_exceptions باید شئ‌ای از کلاس ExceptionProxy باشد.')
        self.assertEqual(user_ls[10].message, "", '\nخطای مورد نظر پیغامی ندارد.')
        self.assertEqual(user_ls[10].function.__name__, "h", '\nخطای مورد نظر در تابع h اتفاق می‌افتد.')