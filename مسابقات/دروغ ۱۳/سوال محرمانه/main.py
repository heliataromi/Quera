from itertools import permutations


alphabet = list('اپتثچحخدذرزژسشصضطظعغفقکگلموهی')
perms = permutations(alphabet)

#s = "سی ذجو نط گقسوشی وز وسگوگ تپنپ ب جثسا جاجونز گوگی جن‌ذبگ. وز ذجو جن‌حبوینج سسگ وز جکاس طکگق ونق وسگوگ سی تبکا تسبگن، سگگ ضبجنق کو ظوه طقنگ."
s = "جن‌حبوینج"
s = list(s)
for perm in perms:
    new_s = []
    for letter in s:
        if letter == 'ب':
            new_s.append('و')
        elif letter == 'ج':
            new_s.append('م')
        elif letter == 'ن':
            new_s.append('ي')
        elif letter in alphabet:
            new_s.append(perm[alphabet.index(letter)])
        else:
            new_s.append(letter)

    print(''.join(new_s))
