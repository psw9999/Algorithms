import sys
from collections import deque

input = sys.stdin.readline

move = [(1,0),(0,1),(-1,0),(0,-1)]
R,C,K = map(int, input().rstrip().split())
graph = []

# 맵 입력받기
for _ in range(R) :
    graph.append(list(input().rstrip()))

# y좌표, x좌표, 방문한 좌표, 이동거리
queue = deque()
queue.append((R-1, 0, [(R-1, 0)], 1))

# 목표에 도달한 가지수
result = 0

while queue :
    y,x,visited, distance = queue.popleft()
    
    # 이동거리가 K와 같고 목적지에 도착한 경우
    if distance == K :
        if y == 0 and x == (C-1) :
            result += 1
        continue
    
    for my, mx in move :
        dy, dx = y + my, x + mx
        
        if dy < 0 or dx < 0 or dy >= R or dx >= C :
            continue
            
        if graph[dy][dx] == 'T' :
            continue
        
        if (dy,dx) in visited :
            continue
        
        temp = visited[:]
        temp.append((dy,dx))
        queue.append((dy, dx, temp, distance + 1))
        
print(result)