class Proxy:
    def __init__(self, obj):
        self._obj = obj
        self.calls = {}
        self.last_invoked = None

    def __getattr__(self, method_name):
        if hasattr(self._obj, method_name):
            self.calls[method_name] = self.calls.get(method_name, 0) + 1
            self.last_invoked = method_name
            return getattr(self._obj, method_name)

        raise Exception('No Such Method')

    def last_invoked_method(self):
        if self.last_invoked:
            return self.last_invoked

        raise Exception('No Method Is Invoked')

    def count_of_calls(self, method_name):
        return self.calls.get(method_name, 0)

    def was_called(self, method_name):
        if method_name in self.calls:
            return True

        return False
