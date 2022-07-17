numbers = [1, 1, 2, 2, 2, 8]
s = list(map(int, input().split()))
out = []

for i in range(6):
	out.append(numbers[i] - s[i])

print(' '.join(map(str, out)))
