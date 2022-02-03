
import sys
from collections import deque

input = sys.stdin.readline

M,N,H = map(int, input().rstrip().split())

move = [(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)]
graph = []

count = 0
location = []
target = M * N * H

for i in range(H) :
    graph.append([])
    for j in range(N) :
        temp = list(map(int,input().rstrip().split()))
        for z in range(len(temp)) :
            if temp[z] == 1 :
                count += 1
                location.append((i,j,z))
            elif temp[z] == -1 :
                target -= 1
        graph[i].append(temp)

result = 0                
while True :
    if target == count :
        print(result)
        break
    temp = []    
    for l,y,x in location :
        for ml,my,mx in move  :
            dl = l + ml
            dy = y + my
            dx = x + mx
            if 0 <= dl < H and 0 <= dy < N and 0 <= dx < M :
                if graph[dl][dy][dx] == 0 :
                    graph[dl][dy][dx] = 1
                    count += 1
                    temp.append((dl,dy,dx))                
    
    location = temp
    if not len(location) :
        print(-1)
        break
    
    result += 1