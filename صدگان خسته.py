n1 = input()
n2 = input()

if int(n1[::-1]) > int(n2[::-1]):
	print(n2, '<', n1)

elif n1 == n2:
	print(n1, '=', n2)

else:
	print(n1, '<', n2)
