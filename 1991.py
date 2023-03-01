N = int(input())

bin_tree = dict()

for _ in range(N):
    root, l, r = map(str, input().split(' '))
    bin_tree[root] = [l, r]
    
def preorder(bin_tree, root):
    if root != '.':
        print(root, end='')
        preorder(bin_tree, bin_tree[root][0])
        preorder(bin_tree, bin_tree[root][1])
    
def inorder(bin_tree, root):
    if root != '.':
        inorder(bin_tree, bin_tree[root][0])
        print(root, end='')
        inorder(bin_tree, bin_tree[root][1])

def postorder(bin_tree, root):
    if root != '.':
        postorder(bin_tree, bin_tree[root][0])
        postorder(bin_tree, bin_tree[root][1])
        print(root, end='')

preorder(bin_tree, 'A')
print()
inorder(bin_tree, 'A')
print()
postorder(bin_tree, 'A')
