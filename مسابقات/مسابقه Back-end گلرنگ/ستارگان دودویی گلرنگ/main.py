ZERO = ['***', '*.*', '***']
ONE = ['.*.', '.*.', '.*.']

n = int(input())
s = input()

out = [[] for i in range(3)]

for x in s:
    if x == '0':
        for i in range(3):
            out[i].append(ZERO[i])

    if x == '1':
        for i in range(3):
            out[i].append(ONE[i])

print('\n'.join([''.join(x) for x in out]))
