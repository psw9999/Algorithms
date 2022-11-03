import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

N,M = map(int, input().rstrip().split())
roads = [[] for _ in range(N+1)]

for _ in range(M) :
    start, end, cost = map(int, input().rstrip().split())
    roads[start].append((end, cost))
    roads[end].append((start, cost))

def dijkstra(start) :
    queue = []
    costs = [INF] * (N+1)
    heapq.heappush(queue, (0, start))
    costs[start] = 0
    
    while queue :
        cost, node = heapq.heappop(queue)

        if cost > costs[node] :
            continue

        for r,c in roads[node] :
            temp_cost = cost + c
            if temp_cost < costs[r] :
                costs[r] = temp_cost
                heapq.heappush(queue, (temp_cost, r))
    
    #print(costs)
    print(costs[N])
        
dijkstra(1)