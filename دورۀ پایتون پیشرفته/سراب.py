n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))
for i in range(n):
    if(lst[i][0] == lst[i][1]):
        if(lst[i][0]%2==0):
            print(2*lst[i][0])
        else:
            print(lst[i][0]*2-1)
    elif(lst[i][0]>1 and lst[i][1]+2==lst[i][0]):
        if(lst[i][0]==2):
            print(2)
        elif(lst[i][0]==3):
            print(3)
        elif(lst[i][0]%2==0):
            print(2 + 2*lst[i][1])
        else:
            print(3 + 2*(lst[i][1]-1))
    else:
        print(-1)
