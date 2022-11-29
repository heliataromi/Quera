from threading import Thread, Lock


def synchronized(f):
    lock = Lock()

    def g(*args, **kwargs):
        lock.acquire()
        f(*args, **kwargs)
        lock.release()
    return g
