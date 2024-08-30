n = int(input())
numbers = list(map(int, input().split()))

ans = 0

for i, number in enumerate(numbers):
    for j, second_number in enumerate(numbers[i+1:]):
        if number > second_number:
            ans += 1

print(ans)
