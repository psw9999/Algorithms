# 내 풀이
# import sys
# from collections import deque

# tetrix = [
#     [(1,0), (0,1), (1,1), (2,1)],
#     [(1,0), (2,0), (0,1), (1,1)],
#     [(0,0), (1,0), (1,1), (2,1)],
#     [(1,0), (0,1), (1,1), (0,2)],
#     [(0,0), (0,1), (1,1), (1,2)],  
#     [(0,0), (1,0), (2,0), (3,0)],
#     [(0,0), (0,1), (0,2), (0,3)],
#     [(0,0), (0,1), (0,2), (1,0)], 
#     [(1,0), (1,1), (1,2), (0,2)],
#     [(0,0), (1,0), (1,1), (1,2)],
#     [(0,0), (0,1), (0,2), (1,2)],
#     [(0,0), (1,0), (2,0), (2,1)],
#     [(2,0), (2,1), (1,1), (0,1)],
#     [(0,0), (0,1), (1,0), (2,0)], 
#     [(0,0), (0,1), (1,1), (2,1)],
#     [(0,0), (0,1), (0,2), (1,1)],
#     [(1,0), (1,1), (1,2), (0,1)],
#     [(0,0), (1,0), (2,0), (1,1)],
#     [(0,0), (0,1), (1,0), (1,1)]  
# ]


# input = sys.stdin.readline
# N,M = map(int,input().rstrip().split())
# graph = []
# for _ in range(N) :
#     graph.append(list(map(int,input().rstrip().split())))

# result = 0
# for y in range(N) :
#     for x in range(M) :
#         for i in range(len(tetrix)) :
#             temp = 0
#             flag = True
#             for tx,ty in tetrix[i] :
#                 dx,dy = tx + x, ty + y
#                 if dx >= M or dy >= N :
#                     flag = False
#                     break
#                 else :
#                     temp += graph[dy][dx]
#             if flag :
#                 result = max(temp, result)

# print(result)

# 다른 방법
import sys
input = sys.stdin.readline
move = [(-1,0),(1,0),(0,-1),(0,1)]
N,M = map(int,input().rstrip().split())
graph = []

def dfs(cnt,temp,x,y) :
    global result, graph, visited
    if cnt == 4 :
        result = max(result, temp)
        return

    if result >= temp + MAX_VALUE * (4-cnt) :
        return
    
    for mx,my in move :
        dx,dy = x+mx, y+my
        if dx < 0 or dy < 0 or dx >= M or dy >= N :
            continue
        if visited[dy][dx] :
            continue
        visited[dy][dx] = True
        if cnt == 2 :
            dfs(cnt+1,temp+graph[dy][dx],x,y)
        dfs(cnt+1,temp+graph[dy][dx],dx,dy)
        visited[dy][dx] = False
    
        
    
MAX_VALUE = 0
for _ in range(N) :
    temp = list(map(int,input().rstrip().split()))
    MAX_VALUE = max(max(temp),MAX_VALUE)
    graph.append(temp)
    
visited = [[False for _ in range(M)] for _ in range(N)]
result = 0
for i in range(N) :
    for j in range(M) :
        visited[i][j] = True
        dfs(1,graph[i][j],j,i)
        visited[i][j] = False

print(result)