from work_place import *


class Mine(WorkPlace):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.expertise = "mine"

    def calc_capacity(self) -> None:
        self.capacity = self.level ** 2

    def calc_costs(self) -> int:
        return Consts.BASE_PLACE_COST + Consts.LEVEL_MUL * self.level
