n = int(input())
k = int(input())
cost = 0

if n < 60 + k:
	cost = n * 1500

else:
	cost = (n - 60 - k) * 3000 + (60 + k) * 1500

print(cost)
