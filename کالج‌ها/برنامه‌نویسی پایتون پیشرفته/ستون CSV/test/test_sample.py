import csv
import unittest

import pandas as pd
from main import calculate_sums


class Test(unittest.TestCase):

    def check(self, correct_csv, user_csv):
        with open(correct_csv) as correct_csv:
            csv_reader = csv.reader(correct_csv, delimiter=',')
            df = pd.DataFrame([csv_reader], index=None)
            df.head()
        row_count = sum(1 for row in df)
        correct_list = [['3', '4', '7'], ['3', '347', '350'], ['322', '321', '643'], ['333', '32', '365']]

        with open(user_csv) as user_csv:
            csv_reader = csv.reader(user_csv, delimiter=',')
            df = pd.DataFrame([csv_reader], index=None)
            df.head()
        row_count = sum(1 for row in df)
        user_list = []
        for i in range(row_count):
            for li in df[i]:
                new_li = []
                for new_char in li:
                    if new_char != " ":
                        new_li.append(new_char.strip())
                user_list.append(new_li)
        return correct_list == user_list

    def test_sample_1(self):
        calculate_sums("test1_sample.csv")
        self.assertTrue(self.check("test/correct_result.csv", "result.csv"))
