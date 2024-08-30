from person import *
from math import sqrt, floor

class Teacher(Person):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__(name, age)
        self.job = "teacher"

    def get_price(self):
        return Consts.BASE_PRICE[self.job] - (self.age - Consts.MIN_AGE) * Consts.AGE_MUL

    def calc_life_cost(self):
        return Consts.BASE_COST[self.job] + (self.age - Consts.MIN_AGE) * Consts.AGE_MUL

    def calc_income(self):
        return Consts.BASE_INCOME[self.job][self.work_place.get_expertise()] - (self.age - Consts.MIN_AGE) * Consts.AGE_MUL
    
