from collections import deque
import sys

def bfs() :
    global N, graph, move
    visited = [[False] * N for _ in range(N)]
    result = 0

    for i in range(N) :
        for j in range(N) :
            if visited[i][j] == False :
                result += 1
                queue = deque()
                queue.append((graph[i][j],i,j))
                visited[i][j] = True
                while queue :
                    color, y, x = queue.popleft()
                    for mx, my in move :
                        dx = mx + x
                        dy = my + y
                        if dx < 0 or dy < 0 or dx >= N or dy >= N :
                            continue
                        if graph[dy][dx] == color and visited[dy][dx] == False :
                            visited[dy][dx] = True
                            queue.append((color,dy,dx))
    
    print(result,end=' ')
    
    
input = sys.stdin.readline
move = [(1,0),(0,1),(-1,0),(0,-1)]
N = int(input())
graph = []
for _ in range(N) :
    graph.append(list(input().rstrip()))
bfs()
for i in range(N) :
    for j in range(N) :
        if graph[i][j] == 'G' :
            graph[i][j] = 'R'
bfs() 