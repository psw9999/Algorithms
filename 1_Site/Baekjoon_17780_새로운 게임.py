
from operator import truediv
import sys

input = sys.stdin.readline
move = [(0,1),(0,-1),(-1,0),(1,0)]

# 맵 밖이거나 파란칸인지 체크
def checkBlue(dx,dy) :
    global locations
    if dx < 0 or dy < 0 or dy >= N or dx >= N or board[dy][dx] == 2 :
        return True
    else :
        return False
        
def moveAll(x,y,dx,dy) :
    global locations, players
    
    for p in players[y][x] :
        players[dy][dx].append(p)
        locations[p][0] = dy
        locations[p][1] = dx
    
    players[y][x] = []

N, K = map(int, input().rstrip().split())
board = []
for _ in range(N) : 
    board.append(list(map(int, input().rstrip().split())))

players = [[[] for _ in range(N)] for _ in range(N)]
locations = []

for i in range(K) :
    r, c, dir = map(int, input().rstrip().split())
    players[r-1][c-1].append(i)
    locations.append([r-1,c-1,dir-1])

for cnt in range(1000) :
    for i in range(len(locations)) :
        y,x,dir = locations[i]
        
        # 가장 아래 말이 아닌 경우 이동 하지 않음.
        if players[y][x][0] != i : 
            continue
        
        dx,dy = x + move[dir][1], y + move[dir][0]

        # 이동하려는 칸이 바깥이거나 파란칸인지 확인
        if checkBlue(dx,dy) :
            # 방향 반대로 전환
            if locations[i][2] == 0 or locations[i][2] == 2:
                locations[i][2] += 1
            else :
                locations[i][2] -= 1
            dir = locations[i][2]
            dx,dy = x + move[dir][1], y + move[dir][0]

            # 방향 전환해도 바깥이거나 파란칸이면 벗어나기
            if checkBlue(dx,dy) :
                continue
        
        # 이동하려는 칸이 흰 칸인 경우
        if board[dy][dx] == 0 :
            moveAll(x,y,dx,dy)
        
        # 이동하려는 칸이 빨간 칸인 경우
        elif board[dy][dx] == 1 :
            players[y][x].reverse()
            moveAll(x,y,dx,dy)
        
        # 테스트
        for p in players :
            print(p)
        print()
        
        # 이동 후 말이 4개 이상인지 확인
        if len(players[dy][dx]) >= 4 :
            print(cnt+1)
            exit()

print(-1)