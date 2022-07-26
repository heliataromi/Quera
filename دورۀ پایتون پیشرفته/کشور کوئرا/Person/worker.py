from person import *
from math import sqrt, floor

class Worker(Person):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__(name, age)
        self.job = "worker"

    def get_price(self):
        return floor(Consts.BASE_PRICE[self.job] * Consts.MIN_AGE / self.age)

    def calc_life_cost(self):
        return floor(Consts.BASE_COST[self.job] * self.age / Consts.MIN_AGE)

    def calc_income(self):
        return floor(Consts.BASE_INCOME[self.job][self.work_place.get_expertise()] * Consts.MIN_AGE / self.age)
