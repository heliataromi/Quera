def calc(lst):
    lst.sort()
    a=sum(lst)/len(lst)
    b=lst[(len(lst)+1)//2-1] if len(lst)%2==1 else (lst[len(lst)//2-1]+lst[len(lst)//2])/2
    c=max(lst)
    return((a,b,c))
