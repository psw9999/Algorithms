import heapq
import sys
input = sys.stdin.readline
N,M,X = map(int, input().split())

INF = int(1e9)

graph = [[] for _ in range(N+1)]

result = [0] * (N+1)


for i in range(M) :
    n,m,t = map(int,input().split())
    
    graph[n].append((m,t))

def dijkstra(start) :
    temp = [INF] * (N+1)    
    q = []
    heapq.heappush(q, (0, start))
    temp[start] = 0
    while q :
        dist, now = heapq.heappop(q)
        if temp[now] < dist :
            continue
        
        for i in graph[now] :
            cost = dist + i[1]
            
            if cost < temp[i[0]] :
                temp[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    if start == X :
        for i in range(1, N+1) :
            result[i] += temp[i]
    
    else :
        result[start] += temp[X]
    
for i in range(1, N+1) :
    dijkstra(i)


print(result)