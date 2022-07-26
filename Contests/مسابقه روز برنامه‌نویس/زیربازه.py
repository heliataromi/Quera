n, w = map(int, input().split())
weighs = list(map(int, input().split()))
ans = 0
summ = 0
for i in range(n):
    summ = weighs[i]
    for j in range(i+1, n):
        if(summ > ans and summ <= w):
            ans = summ
        summ += weighs[j]
print(ans)
