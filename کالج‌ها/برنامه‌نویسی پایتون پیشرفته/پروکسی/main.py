class Proxy:
    def __init__(self, obj: object) -> None:
        self._obj = obj
        self._last_accessed = None
        self._access_count = dict()

    def __getattr__(self, attribute_name):
        if not hasattr(self._obj, attribute_name):
            raise Exception('No such attribute.')

        self._access_count[attribute_name] = self._access_count.get(attribute_name, 0) + 1
        self._last_accessed = attribute_name
        return getattr(self._obj, attribute_name)

    def last_accessed_attribute(self) -> str:
        if len(self._access_count) == 0:
            raise Exception('No attribute was accessed.')

        return self._last_accessed

    def count_of_accesses(self, attribute_name: str) -> int:
        return self._access_count.get(attribute_name, 0)

    def was_accessed(self, attribute_name: str) -> bool:
        if attribute_name not in self._access_count:
            return False

        return True
