# 모든 L마다 BFS를 실행하여 가장 비용이 컸던 것을 리턴한다.
from collections import deque

n,m = map(int,input().split())
graph = []
move = [(1,0),(-1,0),(0,1),(0,-1)]

# 그래프를 띄워쓰기 없이 입력받을 때 참조
for i in range(n) :
    graph.append(list(input()))

def bfs(i,j) :
    queue = deque()
    queue.append((i,j))
    # 임시로 방문여부를 저장할 배열변수 생성
    visited = [[0]*m for _ in range(n)]
    visited[i][j] = 1
    cnt = 0
    while queue :
        y,x = queue.popleft()
        for mv in move :
            nx = x + mv[0]
            ny = y + mv[1]
            if nx < 0 or ny < 0 or nx >= m or ny >= n :
                continue
            if graph[ny][nx] == 'L' and visited[ny][nx] == 0 :
                queue.append((ny,nx))
                visited[ny][nx] = visited[y][x] + 1
                cnt = max(cnt, visited[ny][nx])
    return cnt-1

result = 0               
for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 'L' :
            result = max(result, bfs(i,j))
            
print(result)
            



    

                     
            
