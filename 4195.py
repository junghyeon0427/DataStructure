from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)

def union(x, y):
    result = 0
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x
        friend_nums[x] += friend_nums[y]

def find(x):
    if parent[x] == x:
        return x
    else:
        tmp = find(parent[x])
        parent[x] = tmp
        return parent[x]

T = int(input())

for _ in range(T):
    F = int(input())
    parent = defaultdict(str)
    friend_nums = defaultdict(int)
    
    for _ in range(F):
        f1, f2 = map(str, input().split(' '))
        if f1 not in parent.keys():
            parent[f1] = f1
            friend_nums[f1] = 1
        if f2 not in parent.keys():
            parent[f2] = f2
            friend_nums[f2] = 1
        
        union(f1, f2)
        print(int(friend_nums[find(f1)]))
