
import sys
input = sys.stdin.readline

global graph, wall
N = int(input().rstrip())
graph = []
wall = [[False for _ in range(N)] for _ in range(N)]
population = 0
for _ in range(N) :
    t = list(map(int, input().rstrip().split()))
    population += sum(t)
    graph.append(t)

# 벽 세우기
def makeWall(x, y, d1, d2, isWalled) :
    global wall
    
    for i in range(d1+1) :
        wall[x+i][y-i] = isWalled
        wall[x+d2+i][y+d2-i] = isWalled
    
    for j in range(d2+1) :
        wall[x+j][y+j] = isWalled
        wall[x+d1+j][y-d1+j] = isWalled

# 각 선거구 합계 구하기
def sumLocation(x,y,d1,d2,locations) :
    global graph, wall
    
    # 1번 선거구
    for i in range(x+d1) :
        for j in range(y+1) :
            if wall[i][j] :
                break 
            locations[0] += graph[i][j]
    
    # 2번 선거구
    for i in range(x+d2+1) :
        for j in range(N-1, y, -1) :
            if wall[i][j] :
                break
            locations[1] += graph[i][j]
    
    # 3번 선거구
    for i in range(x+d1, N) :
        for j in range(y-d1+d2) :
            if wall[i][j] :
                break
            locations[2] += graph[i][j]
    
    # 4번 선거구
    for i in range(x+d2+1, N) :
        for j in range(N-1, y-d1+d2-1, -1) :
            if wall[i][j] :
                break
            locations[3] += graph[i][j]
            
result = int(1e9)
for x in range(N) :
    for y in range(N) :
        for d1 in range(1, N) :
            for d2 in range(1, N) :
                if (x+d1+d2) >= N or (y-d1) < 0 or (y+d2) >= N :
                    continue
                makeWall(x,y,d1,d2,True) 
                locations = [0] * 5
                sumLocation(x,y,d1,d2,locations)
                locations[4] = population - sum(locations)
                result = min(result, max(locations) - min(locations))
                makeWall(x,y,d1,d2,False) 

print(result)
