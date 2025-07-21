r, c = map(int, input().split())
if(c <= 10):
    print("Right", 10-r+1, c)
if(c > 10):
    print("Left", 10-r+1, 20-c+1)
