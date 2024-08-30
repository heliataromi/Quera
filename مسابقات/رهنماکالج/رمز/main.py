k = int(input())
pin = input()

ans = 0

for i in range(k):
	rotor = input()

	if rotor.index(pin[i]) <= 4:
		ans += rotor.index(pin[i])

	else:
		ans += 9 - rotor.index(pin[i])

print(ans)
