import os


def list_files(directory):
    all_files = []

    for *_, files in os.walk(directory):
        for file in files:
            all_files.append(file)

    return all_files


def combet(SAliB_format, sajjad_format, path):
    sajjad = 0
    SAliB = 0

    for *_, files in os.walk(path):
        for file in files:
            if os.path.splitext(file)[-1][1:] == SAliB_format:
                SAliB += 1
            if os.path.splitext(file)[-1][1:] == sajjad_format:
                sajjad += 1

    if sajjad > SAliB:
        return 'Win! Normally!'

    all_files = list_files(path)

    file_names = list(map(lambda x: os.path.splitext(os.path.basename(x))[0], all_files))
    name_count = dict()
    for file_name in file_names:
        name_count[file_name] = file_names.count(file_name)
    name_count = {k: v for k, v in sorted(name_count.items(), key=lambda item: item[1])}

    for name, count in name_count.items():
        new_SAliB = SAliB - all_files.count(name + '.' + SAliB_format)
        new_sajjad = sajjad + count - all_files.count(name + '.' + sajjad_format)

        if new_sajjad > new_SAliB:
            return f'Win! you can win if you cheat on \'{name}\'!'

    return 'Lose! you can\'t win this game!'
