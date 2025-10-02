import math
from typing import Callable


def get_func(ls: list[str]) -> list[Callable]:
    funcs = []
    
    for shape in ls:
        if shape == 'square':
            funcs.append(lambda a: a ** 2)

        if shape == 'circle':
            funcs.append(lambda r: r ** 2 * math.pi)

        if shape == 'rectangle':
            funcs.append(lambda w, h: w * h)

        if shape == 'triangle':
            funcs.append(lambda a, h: 1 / 2 * a * h)

    return funcs
