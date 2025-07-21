import unittest

from main import explore

class ScoreListTest(unittest.TestCase):

    def test_1(self):
        result = {'sample_test_media/a': 1, 'sample_test_media/a/dir': 1}
        self.assertEqual(result, explore("txt", "sample_test_media"), "\nخروجی تابع برای پسوند txt و پوشه‌ی sample_test_media (که در فایل پروژه‌ی اولیه‌ی تمرین قرار دارد) برابر است با \n{'sample_test_media/a': 1, 'sample_test_media/a/dir': 1}")

    def test_2(self):
        result = {'sample_test_media/a/a/b': 1}
        self.assertEqual(result, explore("mkv", "sample_test_media"), "\nخروجی تابع برای پسوند mkv و پوشه‌ی sample_test_media (که در فایل پروژه‌ی اولیه‌ی تمرین قرار دارد) برابر است با\n{'sample_test_media/a/a/b': 1}")
