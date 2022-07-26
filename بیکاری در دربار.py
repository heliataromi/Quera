import re
a=re.split("[^0-9#]+",input())
if("#" in a[2]):
    b=str(int(a[0])+int(a[1]))
    c=a[2].index('#')
    if(re.match(a[2][:c],b) and re.match(a[2][::-1][:a[2][::-1].index("#")],b[::-1])):
        #b=b[c:]
        try:
            #if(c!=len(a[2])-1):
                #b=b[:-(re.search(a[2][c+1:][::-1],b[::-1]).end())]
            print("{} + {} = {}".format(a[0],a[1],b))
        except AttributeError:
            print("-1")
    else:
        print("-1")
if("#" in a[1]):
    b=str(int(a[2])-int(a[0]))
    c=a[1].index('#')
    if(re.match(a[1][:c],b) and re.match(a[1][::-1][:a[1][::-1].index("#")],b[::-1])):
        #b=b[c:]
        try:
            #if(c!=len(a[1])-1):
                #b=b[:-(re.search(a[1][c+1:][::-1],b[::-1]).end())]
            print("{} + {} = {}".format(a[0],b,a[2]))
        except AttributeError:
            print("-1")
    else:
        print("-1")
if("#" in a[0]):
    b=str(int(a[2])-int(a[1]))
    c=a[0].index('#')
    if(re.match(a[0][:c],b) and re.match(a[0][::-1][:a[0][::-1].index("#")],b[::-1])):
        #b=b[c:]
        try:
            #if(c!=len(a[0])-1):
                #b=b[:-(re.search(a[0][c+1:][::-1],b[::-1]).end())]
            print("{} + {} = {}".format(b,a[1],a[2]))
        except AttributeError:
            print("-1")
    else:
        print("-1")

