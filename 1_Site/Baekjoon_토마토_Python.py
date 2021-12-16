
from collections import deque

M,N = map(int,input().split())

graph = []

move =[(1,0),(0,1),(-1,0),(0,-1)]

for _ in range(N) :
    graph.append(list(map(int,input().split())))

queue = deque()

for i in range(N) :
    for j in range(M) : 
        if graph[i][j] == 1 :
            queue.append((j,i,0))

result = 0
while queue :
    x,y,cnt = queue.popleft()
    for mx,my in move :
        dx = x + mx
        dy = y + my
        if dx < 0 or dy < 0 or dx >= M or dy >= N or graph[dy][dx] == -1:
            continue
        if graph[dy][dx] == 0 :
            queue.append((dx,dy,cnt+1))
            graph[dy][dx] = graph[y][x] + 1
    

for i in range(N) :
    for j in range(M) :
        if graph[i][j] == 0 :
            result = -1
            exit(0)
    result = max(result,max(graph[i]))
print(result)
    
        