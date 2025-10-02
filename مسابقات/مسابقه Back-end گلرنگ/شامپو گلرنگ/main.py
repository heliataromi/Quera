import heapq

class Shampoo:
    def __init__(self, index, arrival, remaining):
        self.index = index
        self.arrival = arrival
        self.remaining = remaining

    def __lt__(self, other):
        if self.remaining == other.remaining:
            return self.arrival < other.arrival
        return self.remaining < other.remaining

n = int(input())
shampoos = []
current_time = 0
heap = []

for i in range(n):
    arrival, duration = map(int, input().split())
    shampoo = Shampoo(i + 1, arrival, duration)

    while heap and current_time < arrival:
        remaining_time = arrival - current_time
        current_shampoo = heap[0]

        if current_shampoo.remaining <= remaining_time:
            current_time += current_shampoo.remaining
            heapq.heappop(heap)
        else:
            current_shampoo.remaining -= remaining_time
            current_time = arrival
            break

    heapq.heappush(heap, shampoo)

    if heap:
        print(heap[0].index)
