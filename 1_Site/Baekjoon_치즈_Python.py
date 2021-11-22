# 외부부터 탐색

from collections import deque
n,m = map(int,input().split())

graph = []
move = [(1,0),(-1,0),(0,1),(0,-1)]

for _ in range(n) :
    graph.append(list(map(int, input().split())))

    
def bfs(visited) :
    cnt = 0
    queue = deque()
    queue.append((0,0))
    visited[0][0] = -1
    while queue :
        x,y = queue.popleft()
        for mv in move :
            dx = x + mv[0]
            dy = y + mv[1]
            if dx < 0 or dy < 0 or dx >= m or dy >= n : 
                continue
            if visited[dy][dx] == 0 :
                if graph[dy][dx] == 0 :
                    queue.append((dx,dy))
                else :                  
                    graph[dy][dx] = 0
                    cnt +=1
                visited[dy][dx] = -1
    return cnt

cnt = 0
result = []    
while (1) :
    visited = [[0]*m for _ in range(n)]
    result.append(bfs(visited))
    if result[-1]== 0 :
        break
    cnt += 1
print(cnt)
print(result[-2])
    
