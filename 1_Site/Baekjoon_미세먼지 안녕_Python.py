from collections import deque

R,C,T = map(int,input().split())

graph = []
move = [(0,1),(-1,0),(0,-1),(1,0)]

for _ in range(R) :
    graph.append(list(map(int,input().split())))

tempGraph = []
for i in range(R) :
    tempGraph.append([0] * C)
        
queue = deque()
airC = []
for i in range(R) :
    for j in range(C) :
        if graph[i][j] == -1 :
            airC.append((j,i))
        elif graph[i][j] >= 5 :
            queue.append((j,i))

def airCon () :
    global airC, dirty, graph
    up = airC[0]
    down = airC[1]

    # 위 공기청정기
    # 아래
    temp = graph[up[1]][C-1]
    for i in range(C-1, 1, -1) :
        graph[up[1]][i] = graph[up[1]][i-1]
    graph[up[1]][1] = 0
    
    # 오른쪽
    temp1 = graph[0][C-1]
    for i in range(up[1] - 1) :
        graph[i][C-1] = graph[i+1][C-1]
    graph[up[1]-1][C-1] = temp
    
    # 위쪽
    temp2 = graph[0][0]
    for i in range(C-2) :
        graph[0][i] = graph[0][i+1]
    graph[0][C-2] = temp1
    
    # 왼쪽
    for i in range(up[1]-1, 1, -1) :
        graph[i][0] = graph[i-1][0]
    graph[1][0] = temp2
    
    # 아래 공기청정기
    # 위
    temp = graph[down[1]][C-1]
    for i in range(C-1, 1, -1) :
        graph[down[1]][i] = graph[down[1]][i-1]
    graph[down[1]][1] = 0
    
    # 오른쪽
    temp1 = graph[R-1][C-1]
    for i in range(R-1, down[1] + 1, -1) :
        graph[i][C-1] = graph[i-1][C-1]
    graph[down[1]+1][C-1] = temp
    
    # 아래
    temp2 = graph[R-1][0]
    for i in range(C - 2) :
        graph[R-1][i] = graph[R-1][i+1]
    graph[R-1][C-2] = temp1
    
    # 왼쪽
    for i in range(down[1]+1, R-1) :
        graph[i][0] = graph[i+1][0]
    graph[R-2][0] = temp2

while T > 0 :
    T-=1
    tempGraph = [[0]*C for _ in range(R)]
    while queue :
        x,y = queue.popleft()
        sumDirty = 0
        for mv in move :
            dx = x + mv[0]
            dy = y + mv[1]
            if dx < 0 or dy < 0 or dx >= C or dy >= R :
                continue
            if graph[dy][dx] == -1 :
                continue
            sumDirty += graph[y][x]//5
            tempGraph[dy][dx] += graph[y][x]//5
        tempGraph[y][x] -= sumDirty
            
    for i in range(R) :
        for j in range(C) :
            graph[i][j] += tempGraph[i][j]
            
    airCon()
    
    for i in range(R) :
        for j in range(C) :
            if graph[i][j] >= 5 :
                queue.append((j,i))

result = 0
for i in range(R) :
    for j in range(C) :
        if graph[i][j] > 0 :
            result += graph[i][j]

print(result)
                
            
# 다른 사람 코드 (더 좋은 예)
# import sys

# input = sys.stdin.readline

# r, c, t = map(int, input().split())

# arr = [list(map(int, input().split())) for _ in range(r)]

# up = -1
# down = -1
# # 공기 청정기 위치 찾기
# for i in range(r):
#     if arr[i][0] == -1:
#         up = i
#         down = i + 1
#         break

# # 미세먼지 확산
# def spread():
#     dx = [-1, 0, 0, 1]
#     dy = [0, -1, 1, 0]

#     tmp_arr = [[0] * c for _ in range(r)]
#     for i in range(r):
#         for j in range(c):
#             if arr[i][j] != 0 and arr[i][j] != -1:
#                 tmp = 0
#                 for k in range(4):
#                     nx = dx[k] + i
#                     ny = dy[k] + j
#                     if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != -1:
#                         tmp_arr[nx][ny] += arr[i][j] // 5
#                         tmp += arr[i][j] // 5
#                 arr[i][j] -= tmp

#     for i in range(r):
#         for j in range(c):
#             arr[i][j] += tmp_arr[i][j]

# # 공기청정기 위쪽 이동
# def air_up():
#     dx = [0, -1, 0, 1]
#     dy = [1, 0, -1, 0]
#     direct = 0
#     before = 0
#     x, y = up, 1
#     while True:
#         nx = x + dx[direct]
#         ny = y + dy[direct]
#         if x == up and y == 0:
#             break
#         if nx < 0 or nx >= r or ny < 0 or ny >= c:
#             direct += 1
#             continue
#         arr[x][y], before = before, arr[x][y]
#         x = nx
#         y = ny

# # 공기청정기 아래쪽 이동
# def air_down():
#     dx = [0, 1, 0, -1]
#     dy = [1, 0, -1, 0]
#     direct = 0
#     before = 0
#     x, y = down, 1
#     while True:
#         nx = x + dx[direct]
#         ny = y + dy[direct]
#         if x == down and y == 0:
#             break
#         if nx < 0 or nx >= r or ny < 0 or ny >= c:
#             direct += 1
#             continue
#         arr[x][y], before = before, arr[x][y]
#         x = nx
#         y = ny


# for _ in range(t):
#     spread()
#     air_up()
#     air_down()

# answer = 0
# for i in range(r):
#     for j in range(c):
#         if arr[i][j] > 0:
#             answer += arr[i][j]

# print(answer)