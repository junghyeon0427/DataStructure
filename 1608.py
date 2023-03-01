N = int(input())
tree = list(map(int, input().split(' ')))
num = int(input())

def dfs(node, num):
    if tree[num] == float('inf'):
        return
    else:
        tree[num] = float('inf')
        for i in range(len(tree)):
            if tree[i] == num:
                dfs(tree[i], i)
    
dfs(tree[num], num)

cnt = 0
node_list = list()

for i in range(len(tree)):
    if tree[i] != float('inf') and i not in tree:
        cnt += 1

print(cnt)
