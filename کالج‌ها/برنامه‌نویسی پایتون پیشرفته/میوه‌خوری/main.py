def good_fruits(fruits: tuple[dict]) -> dict[str, int]:
    good = {}
    
    for fruit in fruits:
        if fruit['shape'] == 'sphere' and 300 <= fruit['mass'] <= 600 and 100 <= fruit['volume'] <= 500:
            good[fruit['name']] = good.get(fruit['name'], 0) + 1

    return good

