import unittest
from subprocess import PIPE, run
import subprocess


class TestSampleEasyHard(unittest.TestCase):

    def _get_output(self, file, inp):
        command = ['python3', file]
        ps = subprocess.Popen(('echo', inp), stdout=subprocess.PIPE)
        result = run(command, stdout=PIPE, stderr=PIPE,
                     stdin=ps.stdout, universal_newlines=True)
        ps.kill()
        self.assertEqual(result.returncode, 0,
                         "برنامه شما به درستی اجرا نشد. لطفا از اجرای صحیح برنامه خود اطمینان حاصل فرمایید.")
        return result.stdout.strip()

    def test_sample_code_constraints(self):
        with open('main.py', "r") as f:
            ans = 0
            for line in f:
                line = line.strip()
                if line and line[0] != '#':
                    self.assertNotIn(
                        'exec', line, "کد شما نباید از exec استفاده کند.")
                    self.assertNotIn(
                        ';', line, "کد شما نباید از ; استفاده کند.")
                    ans += 1
            self.assertEqual(1, ans, "طول کد شما نباید بیشتر از یک خط باشد.")

    def test_sample_1(self):
        output = self._get_output('main.py', "35 23 12 31 22 48")
        self.assertEqual(output, "48",
                         "خروجی برنامه شما به ازای ورودی 35 23 12 31 22 48 صحیح نیست، خروجی باید برابر با 48 باشد.")

    def test_sample_2(self):
        output = self._get_output(
            'main.py', "60 47 75 42 41 12 49 94 30 96 15")
        self.assertEqual(output, "12",
                         "خروجی برنامه شما به ازای ورودی 60 47 75 42 41 12 49 94 30 96 15 صحیح نیست، خروجی باید برابر با 12 باشد.")

    def test_sample_3(self):
        output = self._get_output(
            'main.py', "15 65 46 54 101 12 16 84 89 74 98 120")
        self.assertEqual(output, "12 120",
                         "خروجی برنامه شما به ازای ورودی 15 65 46 54 101 12 16 84 89 74 98 120 صحیح نیست، خروجی باید برابر با 12 120باشد.")


if __name__ == '__main__':
    unittest.main()
