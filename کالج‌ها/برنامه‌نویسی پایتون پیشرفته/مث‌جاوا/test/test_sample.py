import unittest, time
from threading import Thread, current_thread

from main import synchronized


class ScoreListTest(unittest.TestCase):

    def test_1(self):
        done = []

        @synchronized
        def f(x):
            time.sleep(x)
            done.append(current_thread().name)

        t = Thread(name='first', target=f, args=(0.6,))
        s = Thread(name='second', target=f, args=(0.3,))

        t.start()
        s.start()

        t.join()
        s.join()

        self.assertEqual(done, ['first', 'second'], '\nترتیب اجرای تردها را باید رعایت کنید. ابتدا ترد first و سپس ترد second اجرا می‌شوند.')

    def test_2(self):
        a = 0

        @synchronized
        def f():
            nonlocal a
            for i in range(400000):
                a = a + 1

        t = Thread(target=f)
        s = Thread(target=f)

        t.start()
        s.start()

        t.join()
        s.join()

        self.assertEqual(a, 800000, '\nابتدا ترد t و سپس ترد s، تابع f را صدا می‌زنند.')