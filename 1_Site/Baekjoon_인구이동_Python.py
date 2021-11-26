from collections import deque

n,l,r = map(int, input().split())
move = [(1,0),(-1,0),(0,1),(0,-1)]
graph = []

for _ in range(n) :
    graph.append(list(map(int,input().split())))

def bfs(j,i) :
    temp = []
    temp.append((j,i))
    queue = deque()
    queue.append((j,i))
    visited[i][j] = 1
    cnt = 1
    sumV = graph[i][j]
    while queue :
        x,y = queue.popleft()
        for mv in move :
            dx = x + mv[0]
            dy = y + mv[1]
            if dx < 0 or dy < 0 or dx >= n or dy >= n or (visited[dy][dx]) :
                continue
            if  l <= abs(graph[y][x] - graph[dy][dx]) <= r :
                sumV += graph[dy][dx]
                visited[dy][dx] = 1
                cnt += 1
                queue.append((dx,dy))
                temp.append((dx,dy))

    if cnt > 1 :
        aver = (sumV // cnt)
        for x,y in temp :
            graph[y][x] = aver
        return 1
    else :
        return 0
    
result = 0
while(1) :
    visited = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n) :
        for j in range(n) :
            if not visited[i][j] :
                cnt += bfs(j,i)
    if(cnt == 0) :
        break
    result += 1
    
print(result)