s = input()
for i in range(len(s)):
    print("{0}{1}".format((i+1)*s[i], s[i+1:]))
