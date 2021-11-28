# 실행속도 빠른 코드와 비교시 deepcopy 유무 차이임
# deepCopy는 속도에 지대한 영향을 끼치므로 웬만하면 지양할 것
from copy import deepcopy
from collections import deque

N,M = map(int,input().split())

direction = [
    [[0],[1],[2],[3]],
    [[0,1],[2,3]],
    [[0,3],[1,3],[1,2],[0,2]],
    [[0,1,3],[1,2,3],[0,1,2],[0,2,3]],
    [[0,1,2,3]]
]

move = [(1,0),(-1,0),(0,1),(0,-1)]

CCTV_list = []
graph = []

for i in range(N) :
    temp = list(map(int, input().split()))
    graph.append(temp)
    for j in range(len(temp)) :
        if 0 < temp[j] < 6:
            CCTV_list.append((temp[j]-1,j,i))

def search(Tgraph, dir, x,y) :
    Sgraph = deepcopy(Tgraph)
    for d in dir :
        tx = x
        ty = y 
        while True :
            dx = tx + move[d][0]
            dy = ty + move[d][1]
            if dx < 0 or dy < 0 or dx >= M or dy >= N or Sgraph[dy][dx] == 6:
                #dir.remove(d)
                break
            else :
                if Sgraph[dy][dx] == 0 :
                    Sgraph[dy][dx] = '#'
                tx = dx
                ty = dy
    return Sgraph
        
def CCTV1(cnt,Cgraph) :
    global result
    
    if cnt == len(CCTV_list) :
        temp = 0
        for g in Cgraph :
            temp += g.count(0)
        result = min(result,temp)
        return
    
    Tgraph = deepcopy(Cgraph)
    CCTV_inform = CCTV_list[cnt]
    for d in direction[CCTV_inform[0]] :
        Sgraph = search(Tgraph, d, CCTV_inform[1], CCTV_inform[2])
        CCTV1(cnt+1, Sgraph)

result = N*M
CCTV1(0, graph)

print(result)