import sys
import heapq

input = sys.stdin.readline

N,M = map(int, input().rstrip().split())
bridges = [[] for _ in range(N+1)]

for _ in range(M) :
    start, end, distance = map(int, input().rstrip().split())
    bridges[start].append((end, distance))
    bridges[end].append((start, distance))
start, end = map(int, input().rstrip().split())

def dijkstra(start, end) :
    distances = [0 for _ in range(N+1)]
    distances[start] = 0
    queue = [(0, start)]

    while queue :
        dis, node = heapq.heappop(queue)
        dis = -dis

        if dis < distances[node] and dis != 0 :
            continue

        for n,d in bridges[node] :

            if dis == 0 :
                distances[n] = d
                heapq.heappush(queue, (-distances[n],n))

            elif distances[n] < dis and distances[n] < d :
                distances[n] = min(dis, d)
                heapq.heappush(queue, (-distances[n],n))
    
    return distances[end]

print(dijkstra(start, end))
