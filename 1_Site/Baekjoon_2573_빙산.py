
import sys
from collections import deque

input = sys.stdin.readline
move = [(1,0),(0,1),(-1,0),(0,-1)]
N,M = map(int, input().rstrip().split())

ice_loc = []
graph = []

# 1. 그래프 입력
for i in range(N) :
    graph.append(list(map(int, input().rstrip().split())))

# 2. 얼음 위치 확인
for i in range(N) :
    for j in range(M) :
        if graph[i][j] != 0 :
            ice_loc.append((i,j))

# 3. 얼음 분리될때까지 탐색
result = 1
while True :
    queue = deque(ice_loc[:])
    temp_graph = [[0 for _ in range(M)] for _ in range(N)]
    
    # 4. 얼음 녹이기
    while queue :
        y,x = queue.popleft()
        cnt = 0

        for my,mx in move :
            dy,dx = y + my, x + mx
            if dy < 0 or dx < 0 or dy >= N or dx >= M :
                continue
            if graph[dy][dx] == 0 :
                cnt += 1

        if cnt >= graph[y][x] :
            #graph[y][x] = 0
            ice_loc.remove((y,x))
        else :
            temp_graph[y][x] = graph[y][x] - cnt
    
    if len(ice_loc) == 0 :
        print(0)
        exit(0)
    
    else :
        graph = temp_graph
        count = 0
        queue.append(ice_loc[0])
        visited = [[False for _ in range(M)] for _ in range(N)]
        visited[ice_loc[0][0]][ice_loc[0][1]] = True
        while queue :
            y,x = queue.popleft()
            count += 1

            for my,mx in move :
                dy,dx = y + my, x + mx
                if dy < 0 or dx < 0 or dy >= N or dx >= M :
                    continue

                if graph[dy][dx] > 0 and visited[dy][dx] == False:
                    queue.append((dy,dx))
                    visited[dy][dx] = True

        if count != len(ice_loc) :
            print(result)
            exit(0)
        result += 1
