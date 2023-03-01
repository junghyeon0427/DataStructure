import heapq

n = int(input())

hq = list()

for _ in range(n):
    lst = list(map(int, input().split()))
    if lst[0] == 0:
        if hq:
            print(-heapq.heappop(hq))
        else:
            print(-1)
    else:
        for i, j in enumerate(lst):
            if i == 0:
                continue
            heapq.heappush(hq, -j)       

