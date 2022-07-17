from math import floor

n, k = map(int, input().split())
ans = 0

for i in range(k):
	n /= 2

print(floor(n))
