import os


def find_name_repetitions(files_without_extensions: list[str]) -> dict[str, int]:
    result = dict()
    
    for file in files_without_extensions:
        result[file] = files_without_extensions.count(file)
    
    return result


def find_extensions(salib_format: str, sajjad_format: str, files: list[str]) -> dict[str, int]:
    extensions = {salib_format: [file.split('.')[-1] == salib_format for file in files].count(True),
                  sajjad_format: [file.split('.')[-1] == sajjad_format for file in files].count(True)}
    
    return extensions


def extension_combat(salib_format: str, sajjad_format: str, path: str) -> str:
    files = []
    for directory in os.walk(path):
        for file in directory[2]:
            files.append(file)

    extensions = find_extensions(salib_format, sajjad_format, files)

    if extensions[sajjad_format] > extensions[salib_format]:
        return 'Win! Normally!'

    files_without_extensions = [os.path.splitext(file)[0] for file in files]
    names_count = find_name_repetitions(files_without_extensions)
    cheat_name, cheat_number = '', 0
    maximum_difference = 0
    for name in names_count.keys():
        new_files = []
        for file in files:
            if file.split('.')[0] == name:
                new_files.append(name + '.' + sajjad_format)
            else:
                new_files.append(file)
        extensions = find_extensions(salib_format, sajjad_format, new_files)
        if extensions[sajjad_format] - extensions[salib_format] >= maximum_difference:
            maximum_difference = extensions[sajjad_format] - extensions[salib_format]
            cheat_name, cheat_number = name, extensions[sajjad_format]

    if cheat_number != 0:
        return f'Win! you can win if you cheat on \'{cheat_name}\'!'

    return 'Lose! you can\'t win this game!'


