import math

class Person:
    
    instances = []
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.level = 1
        self.job = ""
        self.work_place= None
        Person.instances.append(self)

    def calc_income(self):
        pass
    
    def calc_life_cost(self):
        pass
    
    def do_level(self, income):
        return income * math.sqrt(self.level * self.work_place.level)
        
    def calc(self):
        income = self.calc_income()
        cost = self.calc_life_cost()
        return self.do_level(income) - cost

    def get_job(self):
        return self.job

    def upgrade(self):
        self.level += 1

    @staticmethod
    def calc_all():
        c = 0
        for x in Person.instances:
            c += x.calc()
        return c
