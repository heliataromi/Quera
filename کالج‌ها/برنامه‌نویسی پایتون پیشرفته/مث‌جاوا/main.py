from threading import Thread, Lock


def synchronized(func):
    lock = Lock()

    def wrapper(*args, **kwargs):
        with lock:
            func(*args, **kwargs)

    return wrapper

