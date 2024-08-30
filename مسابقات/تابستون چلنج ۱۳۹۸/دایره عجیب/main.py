def lcm(a, b):
	t = a % b
	if t == 0:
		return a
	return a * lcm(b, t) // t


a, b = map(int, input().split())
print(lcm(a, b) // b)
