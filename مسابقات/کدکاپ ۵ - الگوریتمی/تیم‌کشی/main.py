people = []
groups = 0

for i in range(6):
	people.append(int(input()))
	if i % 2 != 0:
		groups += min(people[i - 1:])

print(groups)
