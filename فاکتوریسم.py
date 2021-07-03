class FactorHandler:

    def __init__(self):
        self.factors = dict()

    def add_factor(self, time_format, time, value):
        time = self.change_time_format(time_format, time)
        if time in self.factors.keys():
            self.factors[time] += value
        else:
            self.factors[time] = value

    def remove_all_factors(self, time_format, time):
        time = self.change_time_format(time_format, time)
        self.factors.pop(time)

    def get_sum(self, time_format, start_time, finish_time):
        start_time = self.change_time_format(time_format, start_time)
        finish_time = self.change_time_format(time_format, finish_time)
        sum = 0
        for date, value in sorted(self.factors.items()):
            if start_time <= date <= finish_time:
                sum += value
        return sum


    def change_time_format(self, time_format, time):
        new_format = []
        time_format = time_format.split('/')
        time = time.split('/')
        new_format.append(time[time_format.index('yyyy')])
        new_format.append(time[time_format.index('mm')])
        new_format.append(time[time_format.index('dd')])
        new_format = '/'.join(new_format)
        return new_format


# fh = FactorHandler()
# fh.add_factor("dd/mm/yyyy", "02/10/2019", 10)
# fh.add_factor("dd/mm/yyyy", "03/10/2019", 20)
# fh.add_factor("dd/mm/yyyy", "03/10/2019", 30)
# fh.add_factor("dd/mm/yyyy", "05/10/2019", 5)
# print(fh.get_sum("yyyy/dd/mm", "2019/02/10", "2019/03/10"))
# fh.remove_all_factors("mm/dd/yyyy", "10/03/2019")
# print(fh.get_sum("yyyy/dd/mm", "2019/02/10", "2019/05/10"))
