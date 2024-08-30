def separator(ls):
    evens = list(filter(lambda i: i % 2 == 0, ls))
    odds = list(filter(lambda i: i % 2 == 1, ls))
    return evens, odds
