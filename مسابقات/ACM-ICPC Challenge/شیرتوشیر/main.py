n = int(input())
a = list(map(int, input().split()))

for i in range(n - 1, -1, -1):
	a[i] += sum(a[j] / j for j in range(i + 1, n))

print(list(map(lambda x: round(x, 5), a)))
