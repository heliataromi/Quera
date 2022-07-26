import json

n = int(input())
for i in range(n):
    inp = input()
    if(':=' in inp):
        name = inp[:inp.index(':')]
        js = json.loads(inp[inp.index('=') + 1:])
        print(name,js)
#        print(json.dump(js, name))
#        print(jjj)
    else:
        print(inp[inp.index(' ') + 1:])
#    jsn

