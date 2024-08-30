n, m = map(int, input().split())
stars = 0

for i in range(n):
	line = input()
	stars += line.count('*')

print(stars)
