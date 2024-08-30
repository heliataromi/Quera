import sys


class ExceptionProxy(Exception):
    def __init__(self, msg, function):
        self.msg = msg
        self.function = function


def transform_exceptions(func_ls):
    a = []
    for x in func_ls:
        try:
            x()
            a.append(ExceptionProxy("ok!", x))
        except:
            a.append(ExceptionProxy(str(sys.exc_info()[1]), x))

    return a
