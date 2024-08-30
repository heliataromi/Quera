n, q, l = map(int, input().split())
dataset = {}

for _ in range(n):
    binary, state = input().split()
    dataset[binary] = state

for _ in range(q):
    print(dataset.get(input(), 'Unknown'))
