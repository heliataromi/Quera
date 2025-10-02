import unittest
import generators
from source import guess_generator_iterator


class TestAll(unittest.TestCase):

    def test_correct_generator(self):
        print('test_correct_generator')
        gen = generators.guess_generator_1_correct
        min_value, max_value, num = 1, 100, 50
        lst = guess_generator_iterator(gen, min_value, max_value, num)
        print(lst)
        self.assertGreaterEqual(len(lst), 1)
        self.assertEqual(lst[-1], num)
        for guess in lst:
            self.assertIsInstance(guess, int)

if __name__ == '__main__':
    unittest.main()