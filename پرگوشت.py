n, m = map(int, input().split())
answer = []

for i in range(2):
	answer.append(0)
	for j in range(n):
		answer[i] += input().count('*')

print(' '.join(map(str, answer)))
