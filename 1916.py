import heapq
import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    src, dest, cost = map(int, sys.stdin.readline().split(' '))
    graph[src].append((dest, cost))
    
source, destination = map(int, sys.stdin.readline().split(' '))

dist = [float('inf')] * (N+1)

def dijkstra(s):
    hq = list()
    
    dist[s] = 0
    heapq.heappush(hq, (s, 0))
    
    while hq:
        current_loc, dist_tmp = heapq.heappop(hq)
        
        if dist[current_loc] < dist_tmp:
            continue
        
        for next_info in graph[current_loc]:
            next_loc = next_info[0]
            cost_tmp = dist_tmp + next_info[1]
            if cost_tmp < dist[next_loc]:
                dist[next_loc] = cost_tmp
                heapq.heappush(hq, (next_loc, cost_tmp))

dijkstra(source)

print(dist[destination])
