import unittest

from main import get_func


class ScoreListTest(unittest.TestCase):

    def test_circle(self):
        ls = ['circle', 'circle']
        ls_user = get_func(ls)
        self.assertAlmostEqual(ls_user[0](21), 1385.4423602330987, delta=1e-5,msg='\nتابع مربوط به پیاده‌سازی مساحت دایره را به‌درستی پیاده‌سازی نکرده‌اید.')
        self.assertAlmostEqual(ls_user[1](8.5), 226.98006922186255, delta=1e-5, msg='\nتابع مربوط به پیاده‌سازی مساحت دایره را به‌درستی پیاده‌سازی نکرده‌اید.')

    def test_square(self):
        ls = ['square', 'square']
        ls_user = get_func(ls)
        self.assertAlmostEqual(ls_user[0](21), 441, delta=1e-5, msg='\nتابع مربوط به پیاده‌سازی مساحت مربع را به‌درستی پیاده‌سازی نکرده‌اید.')
        self.assertAlmostEqual(ls_user[1](8.5), 72.25, delta=1e-5, msg='\nتابع مربوط به پیاده‌سازی مساحت مربع را به‌درستی پیاده‌سازی نکرده‌اید.')

    def test_rectangle(self):
        ls = ['rectangle', 'rectangle']
        ls_user = get_func(ls)
        self.assertAlmostEqual(ls_user[0](21, 15.4), 323.4, delta=1e-5, msg='\nتابع مربوط به پیاده‌سازی مساحت مستطیل را به‌درستی پیاده‌سازی نکرده‌اید.')
        self.assertAlmostEqual(ls_user[1](8.5, 300), 2550, delta=1e-5, msg='\nتابع مربوط به پیاده‌سازی مساحت مستطیل را به‌درستی پیاده‌سازی نکرده‌اید.')

    def test_triangle(self):
        ls = ['triangle', 'triangle']
        ls_user = get_func(ls)
        self.assertAlmostEqual(ls_user[0](13, 45), 292.5, delta=1e-5, msg='\nتابع مربوط به پیاده‌سازی مساحت مثلث را به‌درستی پیاده‌سازی نکرده‌اید.')
        self.assertAlmostEqual(ls_user[1](8.5, 300), 1275, delta=1e-5, msg='\nتابع مربوط به پیاده‌سازی مساحت مثلث را به‌درستی پیاده‌سازی نکرده‌اید.')

    def test_mixed(self):
        ls = ['circle', 'square', 'triangle', 'triangle', 'rectangle', 'circle']
        ls_user = get_func(ls)
        self.assertAlmostEqual(ls_user[0](21), 1385.4423602330987, delta=1e-5, msg='\nتابع مربوط به پیاده‌سازی مساحت دایره را به‌درستی پیاده‌سازی نکرده‌اید.')
        self.assertAlmostEqual(ls_user[1](8.5), 72.25, delta=1e-5, msg='\nتابع مربوط به پیاده‌سازی مساحت مربع را به‌درستی پیاده‌سازی نکرده‌اید.')
        self.assertAlmostEqual(ls_user[2](8.5, 21), 89.25, delta=1e-5, msg='\nتابع مربوط به پیاده‌سازی مساحت مثلث را به‌درستی پیاده‌سازی نکرده‌اید.')
        self.assertAlmostEqual(ls_user[3](21, 43), 451.5, delta=1e-5, msg='\nتابع مربوط به پیاده‌سازی مساحت مثلث را به‌درستی پیاده‌سازی نکرده‌اید.')
        self.assertAlmostEqual(ls_user[4](21, 12), 252, delta=1e-5, msg='\nتابع مربوط به پیاده‌سازی مساحت مستطیل را به‌درستی پیاده‌سازی نکرده‌اید.')
        self.assertAlmostEqual(ls_user[5](8.123), 207.2921133272676, delta=1e-5, msg='\nتابع مربوط به پیاده‌سازی مساحت دایره را به‌درستی پیاده‌سازی نکرده‌اید.')