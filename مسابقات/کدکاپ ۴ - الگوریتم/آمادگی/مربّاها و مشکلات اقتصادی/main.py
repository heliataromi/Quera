from math import ceil

n, k = map(int, input().split())
fillings = list(map(int, input().split()))

print(n - ceil(sum(fillings) / k))
