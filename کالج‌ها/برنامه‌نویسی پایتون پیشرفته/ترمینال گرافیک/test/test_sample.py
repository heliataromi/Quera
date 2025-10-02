import unittest, os
import time


class TestPygame(unittest.TestCase):

    @staticmethod
    def send_input(inputs):
        with open('input.txt', 'w') as f:
            f.write(inputs)
        os.system('python3 main.py < input.txt')
        time.sleep(2)
        os.system('python3 solution.py < input.txt')
        time.sleep(2)

    def __test_drawing(self):
        with open('solution_draw.png', 'rb') as f:
            quera_drawing = f.read()
        with open('draw.png', 'rb') as f:
            user_drawing = f.read()
        self.assertEqual(user_drawing, quera_drawing, '\nتصویر نهایی کدتان، برابر با تصویر موردنظر نیست.')

    def test_draw_line(self):
        commands = [
            'change size 10',
            'change color 25 25 25',
            'draw line 0 0 100 100',
            'draw line 10 0 100 100',
            'end drawing'
        ]
        TestPygame.send_input('\n'.join(commands))
        self.__test_drawing()