from re import findall


s = input()

vowels = ['a', 'o', 'e', 'u', 'i']

print(len(findall('[aoeui]', s)))
