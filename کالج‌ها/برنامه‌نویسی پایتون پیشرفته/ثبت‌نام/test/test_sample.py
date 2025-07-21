import unittest
from main import check_registration_rules


class TestSampleCheckRegistrationRules(unittest.TestCase):

    def test_return_types(self):
        self.assertTrue(type(check_registration_rules(username='password')) is list,
                        "خروجی کد شما باید از جنس لیست باشد.")
        self.assertTrue(type(check_registration_rules()) is list,
                        "خروجی کد شما باید از جنس لیست باشد.")
        self.assertTrue(type(check_registration_rules(salib='1234567')) is list,
                        "خروجی کد شما باید از جنس لیست باشد.")

    def test_valid_inputs(self):
        output = check_registration_rules(username='password', sadegh='He3@lsa', quera='kLS45@l$')
        self.assertListEqual(['username', 'sadegh'], output,
                             "خروجی تابع به ازای ورودی (username='password', sadegh='He3@lsa', quera='kLS45@l$') باید ['username', 'sadegh'] باشد.")

    def test_invalid_inputs(self):
        output = check_registration_rules(saeed='1234567', ab='afj$L12')
        self.assertListEqual([], output, "خروجی تابع به ازای ورودی (saeed='1234567', ab='afj$L12') باید [] باشد.")
