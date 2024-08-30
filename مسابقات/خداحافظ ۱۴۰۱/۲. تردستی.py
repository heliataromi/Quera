t = int(input())

for _ in range(t):
	cards = input()
	back_cards = [interval for interval in cards.split('1') if interval != '']
	print(len(back_cards))
