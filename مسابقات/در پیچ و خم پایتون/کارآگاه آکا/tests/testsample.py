from django.test import TestCase
import os
import time

from ..solution import Detective


class SampleTestCases(TestCase):

    @classmethod
    def setUpClass(cls):
        super(SampleTestCases, cls).setUpClass()
        os.system("python manage.py makemigrations")
        os.system("python manage.py migrate")
        os.system("python manage.py loaddata setup_test.json")
        os.system("python manage.py runserver &")
        time.sleep(4)

    def test_login(self):

        self.user_audrina = Detective()
        self.assertDictEqual(
            self.user_audrina.login(
                "audrina", "a24011381", "http://127.0.0.1:8000/login/"),
            {"full_name": "Audrina Ebrahimi", "email": "adrina@quera.org"}
        )
