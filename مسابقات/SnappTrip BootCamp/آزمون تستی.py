n = int(input())
key = input()
k = int(input())
answers = []

for i in range(k):
	answers.append([])
	for j in range(n):
		answers[i].append(input())


for answer_sheet in answers:
	t = 0
	f = 0
	for i in range(n):
		if answer_sheet[i].count('#') == 1:
			if answer_sheet[i].index('#') == 0 and key[i] == 'A':
				t += 1
			elif answer_sheet[i].index('#') == 1 and key[i] == 'B':
				t += 1
			elif answer_sheet[i].index('#') == 2 and key[i] == 'C':
				t += 1
			elif answer_sheet[i].index('#') == 3 and key[i] == 'D':
				t += 1
			else:
				f += 1

		if answer_sheet[i].count('#') > 1:
			f += 1

	print(3 * t - f)
