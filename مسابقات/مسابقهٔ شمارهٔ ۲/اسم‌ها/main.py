n = int(input())
numbers = []

for i in range(n):
	numbers.append(len(set(input())))

print(max(numbers))
