import os
def explore(frmt, address):
    out = dict()
    lst = list(os.walk(address))
    for dr in lst:
        c = 0
        for file in dr[2]:
            if ('.' in file):
                if (file[file.rfind('.') + 1:].lower() == frmt.lower()):
                    c += 1
        if(c != 0):
            out[dr[0]] = c
    return out
