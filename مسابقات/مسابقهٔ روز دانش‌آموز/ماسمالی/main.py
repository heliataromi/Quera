from math import comb

n = int(input())
s = input()

print(comb(2 * n - len(s) - 1, n - s.count('I')))
