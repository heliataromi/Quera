def decorator_builder(validator):
    def decorator(func):
        def ret(*args, **kwargs):
            if validator(*args, **kwargs):
                return func(*args, **kwargs)
            else:
                return 'error'
        return ret
    return decorator
