import re


def solve(equation):
    a, b, c = re.split(r' \+ | = ', equation)

    if '#' in a:
        result = str(int(c) - int(b))
        pattern = f'^{a.replace('#', r'\d*')}$'
        if re.match(pattern, result):
            return f'{result} + {b} = {c}'

    elif '#' in b:
        result = str(int(c) - int(a))
        pattern = f'^{b.replace('#', r'\d*')}$'
        if re.match(pattern, result):
            return f'{a} + {result} = {c}'

    elif '#' in c:
        result = str(int(a) + int(b))
        pattern = f'^{c.replace('#', r'\d*')}$'
        if re.match(pattern, result):
            return f'{a} + {b} = {result}'

    return '-1'
