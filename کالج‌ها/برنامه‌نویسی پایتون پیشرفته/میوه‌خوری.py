def fruits(fruit_list):
    good_fruits = {}
    for fruit in fruit_list:
        if fruit['shape'] == 'sphere' and 300 <= fruit['mass'] <= 600 and 100 <= fruit['volume'] <= 500:
            if fruit['name'] in good_fruits.keys():
                good_fruits[fruit['name']] += 1
            else:
                good_fruits[fruit['name']] = 1

    return good_fruits
