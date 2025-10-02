import unittest
import subprocess


class TestFunctions(unittest.TestCase):
    def _get_output(self, file, inp):
        command = ['python3', file]
        ps = subprocess.Popen(('echo', inp), stdout=subprocess.PIPE)
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                stdin=ps.stdout, universal_newlines=True)
        ps.kill()
        self.assertEqual(result.returncode, 0,
                         "برنامه شما به درستی اجرا نشد. لطفاً از اجرای صحیح برنامهٔ خود اطمینان حاصل فرمایید.")
        return result.stdout.strip()

    def test_1(self):
        out_user = self._get_output('main.py', "4 5 6")
        out_judge = "The plants are grown!\nThe music is played!\nThe meal is cooked!\nSequential execution time: 15.0 seconds\nThe plants are grown!\nThe music is played!\nThe meal is cooked!\nThreaded execution time: 6.0 seconds"
        self.assertEqual(out_judge, out_user, "خروجی برنامهٔ شما صحیح نیست.")


if __name__ == "__main__":
    unittest.main()
