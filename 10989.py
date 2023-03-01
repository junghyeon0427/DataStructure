import sys

N = int(sys.stdin.readline())

nums_table = [0] * 10000

for _ in range(N):
    num = int(sys.stdin.readline())
    nums_table[num-1] += 1

for i in range(len(nums_table)):
    if nums_table[i] == 0:
        continue
    else:
        for _ in range(nums_table[i]):
            print(i+1)
