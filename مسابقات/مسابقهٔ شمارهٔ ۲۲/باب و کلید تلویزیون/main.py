n, x, k = map(int, input().split())
channels = []

for i in range(n):
	channels.append(input())

print(channels[x - 1 - (n - k)])
