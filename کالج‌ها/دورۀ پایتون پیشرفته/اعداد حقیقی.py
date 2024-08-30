import re
try:
    while(True):
        line = input()
        if(re.match(r'^\s*[+-]?(\d+(.\d+)?)([Ee][+-]?\d+)?\s*$',line)):
            print("LEGAL")
        else:
            print("ILLEGAL")
        print(line)
except:
    pass
