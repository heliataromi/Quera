from math import floor, sqrt

from person import Person, Consts


class Engineer(Person):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.job = "engineer"

    def get_price(self) -> int:
        return floor(Consts.BASE_PRICE[self.job] * sqrt(Consts.MIN_AGE / self.age))

    def calc_life_cost(self) -> int:
        return floor(Consts.BASE_COST[self.job] * sqrt(self.age / Consts.MIN_AGE))

    def calc_income(self) -> int:
        return floor(Consts.BASE_INCOME[self.job][self.work_place.get_expertise()] * sqrt(Consts.MIN_AGE / self.age))
