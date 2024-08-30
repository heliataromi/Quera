a = 1
lst = []
while(a != 0):
    a = int(input())
    lst.append(a)
lst.reverse()
lst.remove(0)
for x in lst:
    print(x)
