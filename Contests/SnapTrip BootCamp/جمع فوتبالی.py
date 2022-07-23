t = int(input())
goals = []
for i in range(t):
	goals.append(list(map(int, input().split())))

for game in goals:
	if game[0] + game[2] > game[1] + game[3]:
		print('perspolis')

	elif game[0] + game[2] < game[1] + game[3]:
		print('esteghlal')

	else:
		if game[1] > game[2]:
			print('esteghlal')

		elif game[1] < game[2]:
			print('perspolis')

		else:
			print('penalty')