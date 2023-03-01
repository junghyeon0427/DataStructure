from collections import deque

n, w, l = map(int, input().split(' '))
truck = list(map(int, input().split(' ')))

deq = deque([])

truck_idx = 0
time = 0

while truck_idx < n:
    
    if len(deq) == w:
        deq.popleft()
    
    if sum(deq) + truck[truck_idx] > l:
        deq.append(0)
    
    else:
        deq.append(truck[truck_idx])
        truck_idx += 1

    time += 1

print(time + w)

