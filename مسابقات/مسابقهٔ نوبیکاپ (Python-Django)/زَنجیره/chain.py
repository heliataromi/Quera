class Chain:
    def __init__(self, value):
        self.result = value

    def __call__(self, value):
        if isinstance(self.result, (int, float)) and isinstance(value, (int, float)):
            self.result += value
        elif isinstance(self.result, str) and isinstance(value, str):
            self.result += ' ' + value
        else:
            raise Exception('invalid operation')
        return self

    def __repr__(self):
        if isinstance(self.result, float) and self.result.is_integer():
            return repr(int(self.result))
        return repr(self.result)

    def __eq__(self, other):
        return self.result == other
