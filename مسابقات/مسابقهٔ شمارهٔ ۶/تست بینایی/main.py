n = int(input())
original_string = input()
test_string = input()

out = 0

for i in range(n):
	if original_string[i] != test_string[i]:
		out += 1

print(out)
