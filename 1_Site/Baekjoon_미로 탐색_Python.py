from collections import deque

n,m = map(int,input().split())
graph = []
for _ in range(n) :
    graph.append(list(map(int, input())))
    
move = [(1,0),(-1,0),(0,1),(0,-1)]

queue = deque()
queue.append((0,0))
graph[0][0] = 2

while queue :
    x,y = queue.popleft()
    for mv in move :
        dx = x + mv[0]
        dy = y + mv[1]
        if dx < 0 or dy < 0 or dx >= m or dy >= n :
            continue
        if graph[dy][dx] == 1 :
            queue.append((dx,dy))
            graph[dy][dx] = graph[y][x] + 1
            
print(graph[n-1][m-1]-1)