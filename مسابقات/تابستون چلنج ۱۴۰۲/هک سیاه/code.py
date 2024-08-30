n = int(input())
sum = 0
i = 1
while i * i <= n:
    if n % i == 0:
        sum = sum + i
        sum = sum + (n // i)
    i += 1
if sum % 2 == 1:
    print("Odd")
else:
    print("Even")
