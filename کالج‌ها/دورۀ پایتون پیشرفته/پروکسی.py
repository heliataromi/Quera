class Proxy:
    
    def __init__(self, obj):
        self._obj = obj
        self.calls = dict()
        self.last_invoked = ''

    def __getattr__(self, attr):
        if attr in dir(self._obj):
            if attr in self.calls:
                self.calls[attr] += 1
            else:
                self.calls[attr] = 1
            self.last_invoked = attr
            return getattr(self._obj, attr)
        raise Exception('No Such Method')
        
    def last_invoked_method(self):
        if len(self.calls) == 0:
            raise Exception('No Method Is Invoked')
        return self.last_invoked

    def count_of_calls(self, method_name):
        if not hasattr(self._obj, method_name):
            return 0
        if method_name not in self.calls:
            return 0
        return self.calls[method_name]

    def was_called(self, method_name):
        if method_name in self.calls:
            return True
        return False
