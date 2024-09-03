#def validator(x, *args):
#    return #condition

def decorator(validator):
    def check(func):
        def ret(x, *args):
            if(validator(x, *args)):
                return func(x, *args)
            else:
                return 'error'
        return ret
    return check

#@decorator(validator)
#def f(x, y):
#    return x + y

#print(f(4, 5)) #should print 2.0
#print(f(-4 , 5)) #should print error
