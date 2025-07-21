def parse_csv(path: str):
    with open(path) as csv:
        for row in csv.readlines():
            yield row.strip().split(',')

def calculate_sums(path: str) -> None:
    with open("correct_result.csv", "w") as out_file:
        for row in parse_csv(path):
            row_list = list(map(int, row))
            row_list.append(sum(row_list))
            new_row = ", ".join(list(map(str, row_list)))
            out_file.write(new_row + '\n')

