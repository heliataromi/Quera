from threading import Thread

from functions import f, g, h


def make_threads(func_list):
    threads = []

    for i, func in enumerate(func_list):
        threads.append(Thread(target=func, name = str(i + 1)))

    for t in threads:
        t.start()

    for t in threads:
        t.join()

def threadize() -> None:
    make_threads(f)
    make_threads(g)
    make_threads(h)
