n = int(input())
c = 3
fib_list = [1, 1, 2]
while(fib_list[c-1] + fib_list[c-2] <= n):
    fib_list.append(fib_list[c-1] + fib_list[c-2])
    c += 1
for i in range(1, n+1):
    print("+", end='') if i in fib_list else print("-", end='')
