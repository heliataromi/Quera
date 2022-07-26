import sys

class ExceptionProxy(Exception):
    def __init__(self, msg, function):
        self.msg = msg
        self.function = function

def transform_exceptions(func_ls):
    a = []
    for x in func_ls:
        try:
            #eval('{}{}'.format(x, '()'))
            x()
            a.append(ExceptionProxy("ok!", x))
        except:
            a.append(ExceptionProxy(str(sys.exc_info()[1]), x))
    return(a)
#def f():
#    1/0
#
#def g():
#    pass
#
#tr_ls = transform_exceptions([f, g])
#
#for tr in tr_ls:
#    print("msg: " + tr.msg + "\nfunction name: " + tr.function.__name__)
