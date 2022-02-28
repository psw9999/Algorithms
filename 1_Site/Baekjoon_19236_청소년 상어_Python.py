
from copy import deepcopy
import sys
input = sys.stdin.readline

def sharkMove(y,x,tGraph,tFish,cnt) :
    global move,fish,result

    # 상어가 물고기 먹고 삭제, 상어 위치 표시
    sdir = tGraph[y][x][1]
    cnt += tGraph[y][x][0]
    #tGraph[y][x] = [-1,-1]
    tGraph[y][x][1] = -1
        
    # 물고기 이동
    for i in range(1, len(tFish)) :
        fy, fx = tFish[i]
        
        # 먹힌 물고기
        #if tGraph[fy][fx] == [-1,-1] :
        if tGraph[fy][fx][1] == -1 :
            continue
        
        dir = tGraph[fy][fx][1]
        for j in range(0,8) :
            tdir = (dir+j)%8
            my,mx = move[tdir]
            dy,dx = fy + my, fx + mx
            
            # 할당지역 벗어남
            if dx < 0 or dy < 0 or dx >= 4 or dy >= 4 :
                continue
            
            # 해당 칸에 상어가 있음.
            if dy == y and dx == x :
                continue
            
            # 이동가능한 경우 (빈칸, 물고기) 서로 위치 바꾸기
            tGraph[fy][fx][1] = tdir
            tFish[i], tFish[tGraph[dy][dx][0]] = tFish[tGraph[dy][dx][0]], tFish[i]
            tGraph[dy][dx], tGraph[fy][fx] = tGraph[fy][fx], tGraph[dy][dx]
            break
        
    
    # 상어 이동
    for i in range(1,4):
        my,mx = move[sdir][0] * i, move[sdir][1] * i
        sy,sx = y + my, x + mx
        
        # 맵 밖을 벗어남
        if sy < 0 or sx < 0 or sy >= 4 or sx >= 4:
            break
        
        # 이동하는 칸에 물고기가 없음.
        if tGraph[sy][sx][1] == -1 :
            continue

        sharkMove(sy,sx,deepcopy(tGraph),deepcopy(tFish),cnt)
    
    result = max(result,cnt)
    return
              
# y,x
move = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
graph = []
fish = [[0,0] for _ in range(17)]
shark = [0,0]

for i in range(4) :
    temp = list(map(int,input().rstrip().split()))
    graph.append([])
    for j in range(0,8,2) :
        fish[temp[j]] = [i,j//2]
        graph[i].append([temp[j],(temp[j+1]-1)])

result = 0
sharkMove(0,0,deepcopy(graph),deepcopy(fish),0)
print(result)