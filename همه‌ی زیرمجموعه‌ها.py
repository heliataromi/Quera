#incompelete
def subsets(s):
    #if(s==[]):
        #return([s])
    sets=set()
    sets.add(s)
    tmp_subsets=[]
    print('len',len(s))
    for i in range(len(s)):
        for j in range(i,len(s)):
            print('****',s[i:j])
            tmp_subsets=subsets(s[i:j])#+subsets(s[i:])
            print('---------------',tmp_subsets)
            for subset in tmp_subsets:
                sets.add(subset)
    return(sets)
print(subsets(list(range(1,int(input())+1))))
