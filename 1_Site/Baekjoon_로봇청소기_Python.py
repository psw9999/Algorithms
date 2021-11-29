
N,M = map(int,input().split())

y,x,d = map(int,input().split())

graph = []

direction = [(0,-1),(1,0),(0,1),(-1,0)]

result = 0

cnt = 0

for _ in range(N) :
    graph.append(list(map(int, input().split())))

while True :
    if graph[y][x] == 0 :
        graph[y][x] = 2
        result += 1     
        for g in graph :
            print(g)
        print()
    else :
        cnt += 1
        # 네 방향 모두 탐색시 후진
        if cnt >= 5 :
            dx = x - direction[d][0]
            dy = y - direction[d][1]
            # 후진 방향이 벽인 경우 탐색 끝
            if graph[dy][dx] == 1 :
                break
            # 바라보는 방향 유지하며 한 칸 후진
            x,y = dx, dy
            cnt = 0
        else :
            d = (d - 1) % 4
            dx = x + direction[d][0]
            dy = y + direction[d][1]
            # 왼쪽 방향이 벽이거나 청소된 경우
            if graph[dy][dx] == 1 or graph[dy][dx] == 2:
                continue
            if graph[dy][dx] == 0 :
                cnt = 0
                x,y = dx, dy

print(result)         