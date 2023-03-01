import sys

sys.setrecursionlimit(10**6)

M, N, K = map(int, input().split(' '))

matrix = [[0] * N for _ in range(M)]
pos = list()

for _ in range(K):
    pos.append(list(map(int, input().split(' '))))
    
for i in pos:
    x1, y1 = i[0], i[1]
    x2, y2 = i[2], i[3]

    for j in range(x1, x2):
        for k in range(y1, y2):
            matrix[-(k+1)][j] = 1

def dfs(i, j, width):
    if (i < 0 or i >= len(matrix)) or (j < 0 or j >= len(matrix[0])):
        return width
    if matrix[i][j] == 1:
        return width
    
    matrix[i][j] = 1
    width += 1
    
    width = dfs(i+1, j, width)
    width = dfs(i-1, j, width)
    width = dfs(i, j+1, width)
    width = dfs(i, j-1, width)
    
    return width

width_list = list()

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 0:
            width_list.append(dfs(i, j, width=0))

width_list.sort()

print(len(width_list))

for i in width_list:
    print(i, end=' ')
