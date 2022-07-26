class Proxy:
    
    def __init__(self, obj):
        self._obj = obj
        self.calls = dict()
        self.last_invoked = ''

    def __getattr__(self, attr):
        if(attr in dir(self._obj)):
            if(attr in self.calls):
                self.calls[attr] += 1
            else:
                self.calls[attr] = 1
            self.last_invoked = attr
            return getattr(self._obj, attr)
        else:
            raise Exception('No Such Method')
        
    def last_invoked_method(self):
        if(len(self.calls) == 0):
            raise Exception('No Method Is Invoked')
        else:
            return self.last_invoked

    def count_of_calls(self, method_name):
        if(not hasattr(self._obj, method_name)):
            return 0
        else:
            if(method_name not in self.calls):
                return 0
            else:
                return self.calls[method_name]

    def was_called(self, method_name):
        if(method_name in self.calls):
            return True
        else:
            return False

class Radio():
    def __init__(self):
        self._channel = None
        self.is_on = False
        self.volume = 0

    def get_channel(self):
        return self._channel
        
    def set_channel(self, value):
        self._channel = value

    def power(self):
        self.is_on = not self.is_on

radio = Radio()
radio_proxy = Proxy(radio)
radio_proxy.set_channel(95)
radio_proxy.set_channel(65)
radio_proxy.power()
print(radio_proxy.was_called('set_channel'))
print(radio_proxy.was_called('get_channel'))
print(radio_proxy.was_called('gat_channel'))

print('---------------')
import unittest
class Test(unittest.TestCase):

    def test_sample_3(self):
        proxy = Proxy("Test String")
        proxy.upper()
        print(proxy.was_called("upper"))
        print(proxy.was_called("capitalize"))
        proxy.capitalize()
        print(proxy.was_called("capitalize"))
        print(proxy.was_called("not valid"))
t = Test()
t.test_sample_3()
