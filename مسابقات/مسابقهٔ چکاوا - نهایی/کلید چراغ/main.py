n = int(input())
last_status = 0
switches = 0

for i in range(n):
	if i == 0:
		last_status = int(input())

	else:
		current_status = int(input())
		if last_status != current_status:
			switches += 1
		last_status = current_status

print(switches)
