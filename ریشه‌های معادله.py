import math
a, b, c = map(int, input().split())
print((-b + math.sqrt(b**2 - 4*a*c))/(2*a))
print((-b - math.sqrt(b**2 - 4*a*c))/(2*a))
