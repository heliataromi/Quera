aa=int(input())
a=input().split()
bb=int(input())
b=input().split()
cc=int(input())
c=input().split()
d=set(a+b+c)
week=['shanbe','1shanbe','2shanbe','3shanbe','4shanbe','5shanbe','jome']
for x in d:
    week.remove(x)
print(len(week))
