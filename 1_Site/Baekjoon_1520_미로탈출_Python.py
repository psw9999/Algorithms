import heapq, sys
from collections import deque

input = sys.stdin.readline
move = [(1,0),(0,1),(-1,0),(0,-1)]
# 세로, 가로
M,N = map(int, input().rstrip().split())
graph = []
for _ in range(M) :
    graph.append(list(map(int, input().rstrip().split())))

# bfs 방식
# DP = [[0 for _ in range(N)] for _ in range(M)]
# DP[0][0] = 1
# visited = [[False for _ in range(N)] for _ in range(M)]

# # 높이, X, Y
# queue = []
# queue.append([-graph[0][0],0,0])

# while queue :
#     height, x, y = heapq.heappop(queue)
#     height *= -1
#     for mx,my in move :
#         dx = x + mx
#         dy = y + my
#         if dx < 0 or dy < 0 or dx >= N or dy >= M : 
#             continue
#         if graph[dy][dx] >= height :
#             continue
#         if visited[dy][dx] != True :
#             heapq.heappush(queue, [-graph[dy][dx],dx,dy])
#             visited[dy][dx] = True
#         DP[dy][dx] += DP[y][x]


# dfs 방식
DP = [[-1 for _ in range(N)] for _ in range(M)]

def dfs(x,y) :
    if x == (N-1) and y == (M-1) :
        return 1
    if DP[y][x] != -1 :
        return DP[y][x]
    DP[y][x] = 0
    for mx,my in move :
        dx,dy = x + mx, y + my
        if dx < 0 or dy < 0 or dx >= N or dy >= M :
            continue
        if graph[dy][dx] < graph[y][x] :
            DP[y][x] += dfs(dx,dy)
    
    return DP[y][x]

print(dfs(0,0))