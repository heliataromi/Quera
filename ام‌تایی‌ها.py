def calculator(n, m, li):
	result = 0
	lst = []
	sum_in_list = 0
	for i in range(n):
		if i == n - 1:
			sum_in_list += li[i]
			lst.append(sum_in_list)
			sum_in_list = 0
		elif (i + 1) % m != 0:
			sum_in_list += li[i]
		elif (i + 1) % m == 0:
			sum_in_list += li[i]
			lst.append(sum_in_list)
			sum_in_list = 0

	for i in range(len(lst)):
		print(lst[i])
		if i % 2 == 0:
			result += lst[i]
		else:
			result -= lst[i]

	return result
