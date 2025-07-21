def count_executable_lines(path: str) -> int:
    with open(path, "r") as f:
        result = 0

        for line in f.readlines():
            line = line.strip()
            if line != '' and line[0] != '#':
                result +=1

        return result

