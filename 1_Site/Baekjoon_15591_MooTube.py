
import sys
from collections import deque

input = sys.stdin.readline

INF = int(1e9)
N,Q = map(int, input().rstrip().split())

connections = [[] for _ in range(N+1)]
for _ in range(N-1) :
    p,q,r = map(int, input().rstrip().split())
    connections[p].append((q,r))
    connections[q].append((p,r))

result = []
for i in range(Q) :
    k,start = map(int, input().rstrip().split())
    distances = [INF] * (N+1)
    cnt = 0
    
    queue = deque()
    queue.append(start)
    
    while queue :
        v = queue.popleft()

        for number, distance in connections[v] :
            if number == start :
                continue
            if distances[number] == INF : 
                distances[number] = min(distance, distances[v])
                if distances[number] >= k :
                    cnt += 1
                    queue.append(number)

    result.append(str(cnt))
    
print('\n'.join(result))
    

