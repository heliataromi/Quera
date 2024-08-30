n, k = map(int, input().split())
summation = 0
for i in range(n):
	summation += int(input())

if summation >= k:
	print("YES")

else:
	print("NO")
