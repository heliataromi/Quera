def calculator(n: int, m: int, ls: list[int]) -> int:
    groups = [ls[i:i + m] for i in range(0, n, m)]
    sum_of_groups = list(map(sum, groups))
    
    evens = sum(sum_of_groups[::2])
    odds = sum(sum_of_groups[1::2])
    
    value = evens - odds
    return value

