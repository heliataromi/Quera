n, m = map(int, input().split())

board = [['.'] * m for i in range(n)]

for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            board[i][j] = 'A'

        if i == n - 1 or j == m - 1:
            board[i][j] = 'B'

for i in range(n):
    print(''.join(board[i]))
