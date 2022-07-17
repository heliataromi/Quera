s = list(input())

for i in range(len(s)):
	temp = s
	for j in range(i):
		temp[j] = s[i]
	print(''.join(temp))
