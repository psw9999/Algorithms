
import sys
from collections import deque
input = sys.stdin.readline

move = [[(1,0),(1,1)],[(0,1),(1,1)],[(1,0),(0,1),(1,1)]]

N = int(input().rstrip())
graph = []
for _ in range(N) :
    graph.append(list(map(int, input().rstrip().split())))
    
row_graph = [[0 for _ in range(N)] for _ in range(N)]
col_graph = [[0 for _ in range(N)] for _ in range(N)]
dia_graph = [[0 for _ in range(N)] for _ in range(N)]
row_graph[0][1] = 1

for y in range(N) :
    for x in range(N) :
        if row_graph[y][x] :
            for mx,my in move[0] :
                dx,dy = mx + x, my + y
                if dx >= N or dy >= N or graph[dy][dx] :
                    continue
                if my == 0 :
                    row_graph[dy][dx] += row_graph[y][x]
                else :
                    if graph[dy][dx] != 1 and graph[dy-1][dx] != 1 and graph[dy][dx-1] != 1:  
                        dia_graph[dy][dx] += row_graph[y][x]
        if col_graph[y][x] :
            for mx,my in move[1] :
                dx,dy = mx + x, my + y
                if dx >= N or dy >= N or graph[dy][dx] :
                    continue
                if mx == 0 :
                    col_graph[dy][dx] += col_graph[y][x]
                else :
                    if graph[dy][dx] != 1 and graph[dy-1][dx] != 1 and graph[dy][dx-1] != 1:
                        dia_graph[dy][dx] += col_graph[y][x]
        if dia_graph[y][x] :
            for mx,my in move[2] :
                dx,dy = mx + x, my + y
                if dx >= N or dy >= N or graph[dy][dx] or graph[dy][dx] :
                    continue
                if my == 0 :
                    row_graph[dy][dx] += dia_graph[y][x]
                elif mx == 0 :
                    col_graph[dy][dx] += dia_graph[y][x]
                else :
                    if graph[dy][dx] != 1 and graph[dy-1][dx] != 1 and graph[dy][dx-1] != 1:
                        dia_graph[dy][dx] += dia_graph[y][x]

for row in row_graph :     
    print(row)
print(' ')
for col in col_graph :
    print(col)
print(' ')
for dia in dia_graph :
    print(dia)
print(' ')
print(row_graph[N-1][N-1] + col_graph[N-1][N-1] + dia_graph[N-1][N-1])
                        
                