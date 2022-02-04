
import sys
from collections import deque

input = sys.stdin.readline

# 1,5,6,2
diceVer = deque([0,0,0,0])
# 1,3,6,4
diceWid = deque([0,0,0,0])

move = [(0,0),(1,0),(-1,0),(0,-1),(0,1)]

N,M,x,y,K = map(int,input().rstrip().split())
graph = []

for _ in range(N) :
    graph.append(list(map(int,input().rstrip().split())))

move_list = list(map(int,input().rstrip().split()))

for i in move_list :
    mx,my = move[i][0], move[i][1]

    dx = x + mx
    dy = y + my
    
    if dx < 0 or dy < 0 or dy >= N or dx >= M :
        continue
    
    # 동쪽
    if i == 1 :
        diceWid.appendleft(diceWid.pop())
        diceVer[0] = diceWid[0]
        diceVer[2] = diceWid[2]
    
    # 서쪽
    elif i == 2 :
        diceWid.append(diceWid.popleft())
        diceVer[0] = diceWid[0]
        diceVer[2] = diceWid[2]
        
    # 북쪽
    elif i == 3 :
        diceVer.append(diceVer.popleft())
        diceWid[0] = diceVer[0]
        diceWid[2] = diceVer[2]
    
    # 남쪽
    elif i == 4 :
        diceVer.appendleft(diceVer.pop())
        diceWid[0] = diceVer[0]
        diceWid[2] = diceVer[2]
        
    if graph[dy][dx] == 0 :
        graph[dy][dx] = diceVer[2]
    
    else :
        diceWid[2] = graph[dy][dx]
        diceVer[2] = graph[dy][dx]
        graph[dy][dx] = 0
        
    print(diceWid[0])
    
    x,y = dx,dy


