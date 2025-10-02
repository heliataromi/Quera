sort_key = input()
n = int(input())
words = [input() for _ in range(n)]

words.sort(key=lambda word: [sort_key.find(letter) if letter in sort_key else len(sort_key) for letter in word])

print('\n'.join(words))
