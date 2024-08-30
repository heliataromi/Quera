t, a, b = map(int, input().split())
arar = 0
mama = 0

while t >= 1:
	if t - 1 >= 0:
		arar += 1
		t -= 1 + a

	if t - 1 >= 0:
		mama += 1
		t -= 1 + b

print(arar, mama)
