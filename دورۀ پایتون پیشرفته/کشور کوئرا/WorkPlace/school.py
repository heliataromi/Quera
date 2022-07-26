from work_place import *
from math import floor, sqrt

class School(WorkPlace):

    def __init__(self, name):
        super().__init__(name)
        self.expertise = "school"

    def calc_capacity(self):
        self.capacity = floor(sqrt(self.level))

    def calc_costs(self):
        return Consts.BASE_PLACE_COST * floor(sqrt(self.level))
