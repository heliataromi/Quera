A = []

for i in range(3):
    A.append(list(map(int, input().split())))

debtors = []
creditors = []

for i in range(3):
    credit = 0
    for j in range(3):
        A[i][j] -= min(A[i][j], A[j][i])
        A[j][i] -= min(A[i][j], A[j][i])


for i in range(3):
    print(A[i])
