from json import load


def shift(data, key):
    new_data = [0] * len(data)
    for i, item in enumerate(data):
        new_data[i - key] = item

    return new_data


def process(json_files_paths_list):
    with open('ans.csv', 'w') as csv_file:
        for i, path in enumerate(json_files_paths_list):
            with open(path, 'r') as json_file:
                row_dict = load(json_file)
                row = list(map(int, row_dict.values()))
                row.sort()
                new_row = shift(row, i)
                csv_file.write(','.join(map(str, new_row)) + '\n')
