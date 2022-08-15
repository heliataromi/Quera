from json import loads

variables = {}

n = int(input())
for i in range(n):
    inp = input()

    if ':=' in inp:
        name = inp[:inp.index(' ')]
        value = loads(inp[inp.index(' ') + 3:])
        variables[name] = value

    else:
        variable = inp[inp.index(' ') + 1:inp.index('[')]
        key = loads(inp[inp.index('[') + 1:inp.index(']')])
        print(variables[variable][key])
