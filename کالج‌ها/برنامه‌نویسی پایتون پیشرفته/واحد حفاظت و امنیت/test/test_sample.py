import unittest

from main import Security


class ScoreListTest(unittest.TestCase):

    def test_sample_encrypt_method(self):
        sec = Security()
        self.assertEqual("4812162024", sec.encrypt("dddddd"), '\nبرای ورودی dddddd، خروجی تابع encrypt برابر 4812162024 می‌باشد.')

    def test_sample_is_social_account_info_method_1(self):
        sec = Security()
        self.assertEqual(False, sec.is_social_account_info("Imdb:www.imdb.com/"), '\nبرای ورودی Imdb:www.imdb.com/، خروجی تابع is_social_account_info برابر False می‌باشد.')

    def test_sample_is_social_account_info_method_2(self):
        sec = Security()
        self.assertEqual(True, sec.is_social_account_info("Imdb:www.imdb.com/account"), '\nبرای ورودی Imdb:www.imdb.com/account، خروجی تابع is_social_account_info برابر True می‌باشد.')

    def test_sample_secure_method(self):
        sec = Security()
        param = "Tell me something boy? Are You Happy in this modern world? Imdb:www.imdb.com/account Or do you need more?"
        excp = "Tell me something boy? Are You Happy in this modern world? Imdb:www.imdb.com/13615211420 Or do you need more?"
        self.assertEqual(excp, sec.secure(param), '\nبرای ورودی\nTell me something boy? Are You Happy in this modern world? Imdb:www.imdb.com/account Or do you need more?\nخروجی تابع secure برابر\nTell me something boy? Are You Happy in this modern world? Imdb:www.imdb.com/13615211420 Or do you need more?\nمی‌باشد.')