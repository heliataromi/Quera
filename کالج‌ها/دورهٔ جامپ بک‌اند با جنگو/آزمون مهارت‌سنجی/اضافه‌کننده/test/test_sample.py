import unittest

import source


class TestSample(unittest.TestCase):
    def test_sample_simple(self):
        lst = source.appender(1)
        lst = source.appender(2, lst)
        lst = source.appender(3, lst)
        self.assertEqual(lst, [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
