moves = input()

board = [[0 for _ in range(8)] for __ in range(2)]
i, j = 1, 0
board[i][j] = 1

for move in moves:
    if move == 'F':
        j += 1

    elif move == 'L':
        i -= 1
        j += 1

    elif move == 'R':
        i += 1
        j += 1

    if 0 <= i <= 1 and 0 <= j <= 7:
        board[i][j] = 1
    else:
        print('DEATH')
        break
else:
    for row in board:
        print(''.join(map(str, row)))
