from collections import deque

n = int(input())
number = list(map(int, input().split(' ')))

deq = deque([])

for i in range(len(number)):
    tmp = i - number[i]
    deq.insert(tmp, i+1)

for i in deq:
    print(i, end=' ')
