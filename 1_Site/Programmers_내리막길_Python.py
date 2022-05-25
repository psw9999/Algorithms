
import heapq, sys
from collections import deque

input = sys.stdin.readline
move = [(1,0),(0,1),(-1,0),(0,-1)]
# 세로, 가로
M,N = map(int, input().rstrip().split())
graph = []
for _ in range(M) :
    graph.append(list(map(int, input().rstrip().split())))

DP = [[0 for _ in range(N)] for _ in range(M)]
DP[0][0] = 1
visited = [[False for _ in range(N)] for _ in range(M)]

# 높이, X, Y
queue = []
queue.append([-graph[0][0],0,0])

while queue :
    height, x, y = heapq.heappop(queue)
    height *= -1
    for mx,my in move :
        dx = x + mx
        dy = y + my
        if dx < 0 or dy < 0 or dx >= N or dy >= M : 
            continue
        if graph[dy][dx] >= height :
            continue
        if visited[dy][dx] != True :
            heapq.heappush(queue, [-graph[dy][dx],dx,dy])
            visited[dy][dx] = True
        DP[dy][dx] += DP[y][x]

for d in DP :
    print(d)
print(DP[M-1][N-1])
