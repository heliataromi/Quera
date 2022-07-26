nt=input().split()
a=0
for i in range(int(nt[0])):
    a=0
    for x in input():
        if(x not in nt[1]):
            a+=1
    if(a!=0):
        print("No")
    else:
        print("Yes")
