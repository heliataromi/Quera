from typing import Callable


class ExceptionProxy(Exception):
    def __init__(self, message: str, function: Callable):
        self.message = message
        self.function = function


def transform_exceptions(func_ls: list) -> list[ExceptionProxy]:
    result = []

    for func in func_ls:
        try:
            func()
            exception_proxy = ExceptionProxy('ok!', func)
        except Exception as e:
            exception_proxy = ExceptionProxy(str(e), func)

        result.append(exception_proxy)

    return result

