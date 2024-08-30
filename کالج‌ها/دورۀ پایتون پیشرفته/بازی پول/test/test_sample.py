import unittest
from ..source import Account, Site


class TestAccount(unittest.TestCase):

    def setUp(self):
        self.account1 = Account("Ali_Babaei", "5Dj:xKBA", "0030376459", "09121212121", "SAliB_SAliB@gmail.com")

    def test_init(self):
        self.assertEqual(self.account1.username, "Ali_Babaei", '\nویژگی username از کلاس Account را به درستی مقداردهی نکرده‌اید.')
        self.assertIn('_', self.account1.username, '\nویژگی username از کلاس Account حتما باید شامل کاراکتر _ باشد.')
        self.assertEqual(self.account1.username.count('_'), 1, '\nتعداد تکرار کاراکتر _ در ویژگی username از کلاس Account نباید بیشتر از یکبار باشد.')
        self.assertEqual(self.account1.password, 'aca87bf6767f2dbb19d1d5b5d01e3d07eab8ea0f16741bd70e7c0784f0b3916d', '\nویژگی password از کلاس Account را به درستی مقداردهی نکرده‌اید.')
        self.assertEqual(self.account1.user_id, '0030376459', '\nویژگی user_id از کلاس Account را به درستی مقداردهی نکرده‌اید.')
        self.assertEqual(self.account1.phone, '09121212121', '\nویژگی phone از کلاس Account را به درستی مقداردهی نکرده‌اید.')
        self.assertEqual(self.account1.email, 'SAliB_SAliB@gmail.com', '\nویژگی email از کلاس Account را به درستی مقداردهی نکرده‌اید.')


class TestSite(unittest.TestCase):
    def setUp(self):
        self.site1 = Site("salib.net")

    def test_init_site(self):
        self.assertEqual(self.site1.url, "salib.net", '\nویژگی url از کلاس Site را به درستی مقداردهی نکرده‌اید.')
        self.assertListEqual(self.site1.register_users, [], '\nویژگی register_users از کلاس Site را به درستی مقداردهی نکرده‌اید.')
        self.assertListEqual(self.site1.active_users, [], '\nویژگی active_users از کلاس Site را به درستی مقداردهی نکرده‌اید.')


if __name__ == '__main__':
    unittest.main()