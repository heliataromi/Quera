s = input()
if(all([x in 'YR' for x in s]) or s.count('R') == 3 or s.count('R') == 2 and s.count('Y') == 2):
    print("nakhor lite")
else:
    print("rahat baash")
