import sys
from collections import deque

input = sys.stdin.readline
move = [(1,0),(0,1),(-1,0),(0,-1)]
N,M,K = map(int, input().rstrip().split())
graph = []
for _ in range(N) :
    graph.append(list(input().rstrip()))

visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(K+1)]
visited[0][0][0] = True
queue = deque()

# 벽 부순 횟수, X, Y
queue.append((0,0,0,1))

while queue :
    b,x,y,cnt = queue.popleft()
    if x == M-1 and y == N-1 :
        print(cnt)
        exit()
    
    for mx,my in move :
        dx,dy = x + mx, y + my
        if dx < 0 or dy < 0 or dx >= M or dy >= N :
            continue
        if graph[dy][dx] == '1' and b < K and visited[b+1][dy][dx] == False:
            queue.append((b+1,dx,dy,cnt+1))
            visited[b+1][dy][dx] = True
            visited[b+1][y][x] = True
        elif graph[dy][dx] == '0' and visited[b][dy][dx] == False:
            queue.append((b,dx,dy,cnt+1))
            visited[b][dy][dx] = True
            
print(-1)
