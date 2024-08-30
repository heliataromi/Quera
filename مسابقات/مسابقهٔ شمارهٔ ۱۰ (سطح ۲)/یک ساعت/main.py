a, b = map(int, input().split())
h = (12 - a) % 12
m = (60 - b) % 60

print(str(h).zfill(2) + ':' + str(m).zfill(2))
