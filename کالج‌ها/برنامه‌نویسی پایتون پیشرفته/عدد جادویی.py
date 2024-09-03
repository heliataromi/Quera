class Strint(int):

    def __lt__(self, other):
        return self % 10 < other % 10

    def __gt__(self, other):
        return self % 10 > other % 10

    def __le__(self, other):
        return self % 10 <= other % 10

    def __ge__(self, other):
        return self % 10 >= other % 10

    def __eq__(self, other):
        return self % 10 == other % 10

    def __ne__(self, other):
        return self % 10 != other % 10

    def __add__(self, other):
        return int(str(self) + str(other))

    def __sub__(self, other):
        if len(other) > len(self):
            raise Exception('The subtraction is not valid!')
        if not str(self).endswith(str(other)):
            raise Exception('The subtraction is not valid!')
        if len(self) == len(other):
            return 0
        return int(str(self)[:-len(str(other))])

    def __len__(self):
        return len(str(self))

    def __call__(self):
        fa = '۰۱۲۳۴۵۶۷۸۹'
        en = '0123456789'
        out = ''
        for digit in str(self):
            out += fa[en.index(digit)]
        return out
