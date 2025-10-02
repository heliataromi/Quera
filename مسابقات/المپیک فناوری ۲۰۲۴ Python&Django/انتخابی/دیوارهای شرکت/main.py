n = int(input())
intervals = []

perimeter = 0

for _ in range(n):
    l, r = map(int, input().split())
    intervals.append((l, r))

for i, interval in enumerate(intervals):
    l_i, r_i = interval

    for j in range(l_i, r_i):
        if j == l_i:
            perimeter += 1
        if j == r_i - 1:
            perimeter += 1
        if i == 0 or j < intervals[i - 1][0] or j >= intervals[i - 1][1]:
            perimeter += 1
        if i == n - 1 or j < intervals[i + 1][0] or j >= intervals[i + 1][1]:
            perimeter += 1

print(perimeter)
