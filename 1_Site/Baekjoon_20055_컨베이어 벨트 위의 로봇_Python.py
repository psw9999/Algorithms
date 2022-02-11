
import sys
from collections import deque
input = sys.stdin.readline

N,K = map(int,input().rstrip().split())
L = N * 2
#visited = deque([False] * N)
belt = deque(map(int, input().rstrip().split()))
belts = deque()
for b in belt :
    belts.append([False,b])
    
grade = 1
queue = deque()
total = 0
while True :
    #visited.rotate(1)
    #belt.rotate(1)
    belts.rotate(1)
    temp = deque()
    while queue :
        c = queue.popleft()+1
        if c == N - 1 :
            #visited[c] = False
            belts[c][0] = False
            continue
        if belts[c+1][0] == False and belts[c+1][1] >= 1 :
            belts[c+1][1] -= 1
            if belts[c+1][1] == 0 :
                total += 1
            belts[c][0] = False
            if c+1 != N-1 :
                belts[c+1][0] = True
                temp.append(c+1)
        else :
            temp.append(c)

    if belts[0][0] == False and belts[0][1] >= 1 :
        belts[0][0] = True
        belts[0][1]-=1
        if belts[0][1] == 0 :
            total+=1
        temp.append(0)
     
    if total >= K :
        print(grade)
        break
    grade += 1
    queue = temp