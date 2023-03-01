import sys

lst = list()

n, m = map(int, sys.stdin.readline().split(' '))

for _ in range(m):
    lst.append(list(map(int, sys.stdin.readline().split(' '))))

parent = [i for i in range(n)]

def find(x):
    if parent[x] == x:
        return x
    else:
        return find(parent[x])

def union(x, y):
    x = find(x)
    y = find(y)
    if x > y:
        parent[x] = y
    else:
        parent[y] = x

cnt = 0
flag = 0

for a, b in lst:
    cnt += 1
    if find(a) == find(b):
        result = cnt
        flag = 1
        break
    else:
        union(a, b)
        
if flag == 0:
    print(0)
else:
    print(result)
