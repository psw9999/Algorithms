
import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

def blockMove(Tgraph,TBlock,dir,cnt) :
    global move, result,blocks
    if cnt == 5:
        return
    
    mx,my = move[dir][0], move[dir][1]
    
    visited = [[False] * N for _ in range(N)]
    
    while TBlock :
        if dir >= 2 :
            x,y = TBlock.pop()
            dx = x + mx
            dy = y + my
            
            if dx < 0 or dy < 0 or dx >= N or dy >= N or visited[dy][dx]:
                continue
            
            if Tgraph[dy][dx] == Tgraph[y][x] :
                Tgraph[dy][dx] += Tgraph[y][x]
                Tgraph[y][x] = 0
                visited[dy][dx] = True
            
            elif Tgraph[dy][dx] == 0 :
                Tgraph[dy][dx] = Tgraph[y][x]
                Tgraph[y][x] = 0
                TBlock.append((dx,dy))
            
            else :
                continue
            
        else :
            x,y = TBlock.popleft()
            dx = x + mx
            dy = y + my
            
            if dx < 0 or dy < 0 or dx >= N or dy >= N or visited[dy][dx]:
                continue
            
            if Tgraph[dy][dx] == Tgraph[y][x] :
                Tgraph[dy][dx] += Tgraph[y][x]
                Tgraph[y][x] = 0
                visited[dy][dx] = True
            
            elif Tgraph[dy][dx] == 0 :
                Tgraph[dy][dx] = Tgraph[y][x]
                Tgraph[y][x] = 0
                TBlock.appendleft((dx,dy))
                
            else :
                continue
    
    temp = deque()
    for i in range(N) :
        for j in range(N) :
            if Tgraph[i][j] != 0 :
                result = max(Tgraph[i][j],result)
                temp.append((j,i))
    
    # for g in Tgraph :
    #     print(g)
    # print()
    
    for i in range(4) :
        tG = deepcopy(Tgraph)
        tB = deepcopy(temp)
        blockMove(tG,tB,i,cnt+1)
    
N = int(input())

move = [(-1,0),(0,-1),(1,0),(0,1)]
graph = []

for _ in range(N) :
    graph.append(list(map(int,input().rstrip().split())))
    
blocks = deque()
result = 0
for i in range(N) :
    for j in range(N) :
        if graph[i][j] != 0 :
            result = max(graph[i][j],result)
            blocks.append((j,i))

for i in range(4) :
    tempGraph = deepcopy(graph)
    tempBlock = deepcopy(blocks)
    blockMove(tempGraph,tempBlock,i,0)
# blockMove(graph,blocks,1,0)

print(result)