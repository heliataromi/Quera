import os
from collections import Counter


def multimode(data):
    counts = Counter(iter(data))
    if not counts:
        return []
    maxcount = max(counts.values())
    return [value for value, count in counts.items() if count == maxcount]


def find_extensions(type1, type2, files):
    extensions = {type1: [os.path.splitext(file)[1][1:] == type1 for file in files].count(True),
                  type2: [os.path.splitext(file)[1][1:] == type2 for file in files].count(True)}
    return extensions


def combet(type1, type2, path):
    files = []
    for directory in os.walk(path):
        for file in directory[2]:
            files.append(file)

    extensions = find_extensions(type1, type2, files)

    if extensions[type2] > extensions[type1]:
        return 'Win! Normally!'

    files_without_extensions = [os.path.splitext(file)[0] for file in files]
    most_names = multimode(files_without_extensions)
    cheat_name, cheat_number = '', 0

    for name in most_names:
        if files.count(name + '.' + type1) >= cheat_number:
            cheat_name = name
            cheat_number = files.count(name + '.' + type1)

    for i in range(len(files)):
        if os.path.splitext(files[i])[0] == cheat_name:
            files[i] = cheat_name + '.' + type2

    extensions = find_extensions(type1, type2, files)

    if extensions[type2] > extensions[type1]:
        return f'Win! you can win if you cheat on \'{cheat_name}\'!'

    return 'Lose! you can\'t win this game!'
