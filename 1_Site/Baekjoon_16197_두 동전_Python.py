import sys
from collections import deque

input = sys.stdin.readline
move = [(1,0),(0,1),(-1,0),(0,-1)]
N,M = map(int, input().rstrip().split())

visited = [[[[False for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)]

graph = []
for _ in range(N) :
    graph.append(list(input().rstrip()))
    
queue = deque()
temp = [0]
for i in range(N) :
    for j in range(M) :
        if graph[i][j] == 'o' :
            temp.append((j,i))

cnt,(tx1,ty1),(tx2,ty2) = temp
visited[ty1][tx1][ty2][tx2] = True

queue.append(temp)

# 움직인 횟수, 동전1 위치, 동전2 위치
while queue :
    cnt, (x1, y1), (x2, y2) = queue.popleft()
    
    # 10번보다 많이 눌러야 하는 경우
    if cnt >= 10 :
        continue
    
    for mx,my in move :
        dx1,dy1,dx2,dy2 = x1 + mx, y1 + my, x2 + mx, y2 + my
        
        # 둘 다 맵에서 벗어난 경우
        if (dx1 < 0 or dy1 < 0 or dx1 >= M or dy1 >= N) and (dx2 < 0 or dy2 < 0 or dx2 >= M or dy2 >= N) :
            continue
        
        # 둘 중 하나만 맵에서 벗어난 경우
        elif (dx1 < 0 or dy1 < 0 or dx1 >= M or dy1 >= N) or (dx2 < 0 or dy2 < 0 or dx2 >= M or dy2 >= N) :
            print(cnt+1)
            exit(0)
        
        # 두가지 모두 맵에서 벗어나지 않은 경우
        else :
            # 이동하려는 칸에 벽이 있는 경우
            if graph[dy1][dx1] == '#' :
                dy1,dx1 = y1,x1
            if graph[dy2][dx2] == '#' :
                dy2,dx2 = y2,x2
            
            # 이동했는데 변화가 없는 경우 무시
            if visited[dy1][dx1][dy2][dx2] :
                continue
            
            queue.append([cnt+1,(dx1,dy1),(dx2,dy2)])
            visited[dy1][dx1][dy2][dx2] = True
print(-1)