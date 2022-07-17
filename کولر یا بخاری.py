n = int(input())
s = list(map(int, input().split()))

for i in range(n):
	if s[i] > 15:
		print('cooler')

	else:
		print('heater')
