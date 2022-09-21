
import sys
from collections import deque

input = sys.stdin.readline
move = [(1,0),(0,1),(-1,0),(0,-1)]

N,M = map(int, input().rstrip().split())
x1,y1,x2,y2 = map(int, input().rstrip().split())
graph = []
for _ in range(N) :
    graph.append(list(input().rstrip()))

result = 0
while True :
    result += 1
    queue = deque()
    visited = [[False for _ in range(M)] for _ in range(N)]
    queue.append((y1-1,x1-1))
    
    while queue :
        x,y = queue.popleft()
        for mx,my in move :
            dx,dy = x + mx, y + my
            if dx < 0 or dy < 0 or dx >= M or dy >= N :
                continue

            if graph[dy][dx] == '1' :
                graph[dy][dx] = '0'
                visited[dy][dx] = True
            
            elif graph[dy][dx] == '0' and visited[dy][dx] == False :
                queue.append((dx,dy))
                visited[dy][dx] = True
            
            elif graph[dy][dx] == '#' :
                print(result)
                exit(0)