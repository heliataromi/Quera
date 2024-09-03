def sort_strings(arr: [str]):
    arr.sort(key=lambda name: name[:2])
    arr.sort(key=lambda name: name[0].upper())
    return arr
