from math import floor, sqrt

from work_place import *


class School(WorkPlace):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.expertise = "school"

    def calc_capacity(self) -> None:
        self.capacity = floor(sqrt(self.level))

    def calc_costs(self) -> int:
        return Consts.BASE_PLACE_COST * floor(sqrt(self.level))
