class Chain:
    def __init__(self, value):
        self.result = value

    def __call__(self, value):
        if isinstance(self.result, (int, float)):
            try:
                self.result += value
                return self
            except:
                raise Exception('invalid operation')
        elif isinstance(self.result, str):
            try:
                self.result += ' ' + value
                return self
            except:
                raise Exception('invalid operation')
        raise Exception('invalid operation')

    def __repr__(self):
        if isinstance(self.result, float):
            frac = self.result - int(self.result)
            if frac == 0:
                return str(int(self.result))
        return str(self.result)

    def __eq__(self, other):
        return self.result == other


if __name__ == '__main__':
    print(Chain('Ali')(5))
