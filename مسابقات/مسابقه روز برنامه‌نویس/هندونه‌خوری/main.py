n = int(input())
weights = list(map(int, input().split()))
keep_weights = []
for weight in weights:
	keep_weights.append(weight)
heaviest = 0

for i in range(n - 1):
	temp = weights[:2]
	heaviest = keep_weights.index(max(temp))
	weights.remove(min(temp))

print(heaviest + 1)
