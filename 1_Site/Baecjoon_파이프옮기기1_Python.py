
import sys
input = sys.stdin.readline

def dfs(x,y,dir) :
    global N, graph, result

    if x == (N-1) and y == (N-1) :
        result += 1
        return
    
    if dir == 0 or dir == 2 :
        if x + 1 < N :
            if graph[y][x+1] == 0 :
                dfs(x+1,y,0)
    if dir == 1 or dir == 2 :
        if y + 1 < N :
            if graph[y+1][x] == 0 :
                dfs(x,y+1,1)
    if dir == 0 or dir == 1 or dir == 2 :
        if x+1 < N and y+1 < N :
            if graph[y+1][x] == 0 and graph[y][x+1] == 0 and graph[y+1][x+1] == 0:
                dfs(x+1,y+1,2)
        
    
result = 0
N = int(input())
graph = [list(map(int, input().rstrip().split())) for _ in range(N)]

dfs(1,0,0)

print(result)