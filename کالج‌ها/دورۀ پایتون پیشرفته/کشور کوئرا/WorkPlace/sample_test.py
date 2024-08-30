import unittest, math
from work_place import *
from company import *
from mine import *
from school import *

class ScoreListTest(unittest.TestCase):

    def test_a_scenario_for_mine(self):

        mine = Mine("madane kerman")
        mine.level = 10
        mine.calc_capacity()

        self.assertEqual(Consts.BASE_PLACE_COST + Consts.LEVEL_MUL*10, mine.calc_costs())
        self.assertEqual(100, mine.capacity)

    def test_a_scenario_for_school(self):
        school = School("dabestan akhlagh")
        school.level = 123
        school.calc_capacity()

        self.assertEqual(11, school.capacity)
        self.assertEqual(Consts.BASE_PLACE_COST * int(math.sqrt(123)), school.calc_costs())

    def test_a_scenario_for_company(self):
        company = Company("quera")
        company.level = 10
        company.calc_capacity()
        self.assertEqual(10, company.capacity)
        self.assertEqual(Consts.BASE_PLACE_COST * 10, company.calc_costs())
