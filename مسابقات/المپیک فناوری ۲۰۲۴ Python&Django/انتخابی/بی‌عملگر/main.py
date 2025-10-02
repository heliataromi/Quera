import operator

a, b, c = map(int, input().split('?'))

maximum = 0

OPERATORS = (operator.add, operator.mul)

for x in (((a, b), c), ((b, c), a)):
    for op in OPERATORS:
        for op2 in OPERATORS:
            if op2(op(*x[0]), x[1]) > maximum:
                maximum = op2(op(*x[0]), x[1])

print(maximum)
