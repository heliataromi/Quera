def csv_reader(path):
    with open(path) as csv:
        for row in csv.readlines():
            yield row.rstrip().split(', ')
def process(path):
    file = open("ans.csv", "w")
    for x in csv_reader(path):
        a = list(map(int, x))
        a.append(sum(a))
        file.write(", ".join(list(map(str, a))) + '\n')
    file.close()
        
