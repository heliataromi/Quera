key = input()
q = int(input())

found = False

for _ in range(q):
    guess = input()

    if found:
        result = 'Game Over'

    elif len(guess) != len(key):
        result = 'Invalid Length'

    else:
        resulted = {letter: 0 for letter in guess}
        result = [''] * len(guess)

        for i, letter in enumerate(guess):
            if letter == key[i]:
                result[i] = 'G'
                resulted[letter] += 1

        for i, letter in enumerate(guess):
            if result[i] != 'G':
                if letter in key:
                    if resulted[letter] >= key.count(letter):
                        result[i] = 'R'
                        resulted[letter] += 1
                    else:
                        result[i] = 'Y'
                        resulted[letter] += 1
                else:
                    result[i] = 'R'
                    resulted[letter] += 1

        result = ''.join(result)

        if all(r == 'G' for r in result):
            found = True

    print(result)
