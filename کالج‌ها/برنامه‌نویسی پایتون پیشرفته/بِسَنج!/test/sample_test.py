import unittest
from main import *


class TestSampleValidators(unittest.TestCase):

    def test_validate_email(self):
        self.assertTrue(validate_email('test.test91@yahoo.com'), 'ایمیل test.test91@yahoo.com یک ایمیل معتبر است.')
        self.assertFalse(validate_email('exampl#e@gmail.comm'), 'ایمیل exampl#e@gmail.comm یک ایمیل نامعتبر است.')

    def test_validate_phone(self):
        self.assertTrue(validate_phone('09116547899'), 'شماره 09116547899 یک شماره معتبر است.')
        self.assertFalse(validate_phone('091165478999'), 'شماره 091165478999 یک شماره نامعتبر است.')
