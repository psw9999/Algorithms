from collections import deque

N = int(input())

move = [(-1,0),(0,-1),(0,1),(1,0)]

# 상어 크기, 먹은 물고기, 움직인 거리
status = [2,0,0]

graph = [list(map(int,input().split())) for _ in range(N)]

# 상어 현재 위치
cx,cy = 0,0

# 아기상어 현재 위치 찾기 (※ 맨처음 입력 받을 때 아기상어 위치 알아내는법?)
# 다른 사람 코드 봐도 모두 동일함. 방법은 따로 없는듯
for ty in range(N) : 
    for tx in range(N) :
        if graph[ty][tx] == 9 :
            cx,cy = tx,ty
            graph[ty][tx] = 0
            break

# 먹을 수 있는 물고기 탐색
def BFS(visited) :
    global cx,cy,status
    fish = []
    queue = deque()
    queue.append((cx,cy,0))
    while queue :
        x,y,cnt = queue.popleft()
        # 이 부분 추가안하면 시간초과 발생
        if visited[y][x] != 0 :
            continue
        
        visited[y][x] = 1
        if graph[y][x] != 0 and status[0] > graph[y][x]:
            fish.append((cnt,x,y))
        for mv in move :
            dx = x + mv[0]
            dy = y + mv[1]
            if dx < 0 or dy < 0 or dx >= N or dy >= N :
                continue
            if visited[dy][dx] == 0 and status[0] >= graph[dy][dx] :
                queue.append((dx,dy,cnt+1))
    if not fish : 
        return False
    
    fish.sort(key = lambda x : (x[0],x[2],x[1]))
    graph[fish[0][2]][fish[0][1]] = 0
    status[2] += fish[0][0]
    status[1] += 1
    cx,cy = fish[0][1],fish[0][2]
    return True
        
while(1) :
    visited = [[0] * N for _ in range(N)]
        
    if BFS(visited) == False :
        break
    
    # 자신의 크기와 먹은 물고기 수가 같으면 사이즈 업
    if status[1] == status[0] :
        status[1] = 0
        status[0] += 1

print(status[2])

