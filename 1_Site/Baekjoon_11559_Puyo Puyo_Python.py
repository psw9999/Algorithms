
import sys
from collections import deque

input = sys.stdin.readline
move = [(1,0),(0,1),(-1,0),(0,-1)]
graph = []

for i in range(12) :
    graph.append(list(input().rstrip()))

def findZero(x,y,graph) :
    if y == 0 or graph[y][x] != '.' :
        return (x,y)

    else :
        return findZero(x,y-1,graph)

result = 0
while True :
    flag = False
    visited = [[False for _ in range(6)] for _ in range(12)]
    # 같은 블록 탐색
    for i in range(12) :
        for j in range(6) :
            visited[i][j] = True
            if graph[i][j] == '.' :
                continue
            
            elif graph[i][j] != 0 :
                queue = deque()
                queue.append((j,i,graph[i][j]))
                blockList = [(j,i)]
                while queue :
                    x,y,block = queue.popleft()
                    for mx,my in move :
                        dx,dy = x + mx, y + my
                        if dx < 0 or dy < 0 or dx >= 6 or dy >= 12 :
                            continue
                        if visited[dy][dx] :
                            continue
                        if graph[dy][dx] == block :
                            visited[dy][dx] = True
                            queue.append((dx,dy,graph[dy][dx]))
                            blockList.append((dx,dy))

                if len(blockList) >= 4 :
                    flag = True
                    for x,y in blockList :
                        graph[y][x] = '.'

    if not flag :
        break
    # 터진 블록 메꾸기
    else :
        for j in range(6) :
            for i in range(11,-1,-1) :
                if graph[i][j] == '.' :
                    x,y = findZero(j,i,graph)
                    graph[i][j] = graph[y][x]
                    graph[y][x] = '.'
        result += 1

print(result)