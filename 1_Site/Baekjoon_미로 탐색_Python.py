from collections import deque
from itertools import combinations
from copy import deepcopy

n,m = map(int,input().split())
move = [(1,0),(-1,0),(0,1),(0,-1)]

graph = []
virus = []
person = []

result = 0

for i in range(n) :
    graph.append(list(map(int,input().split())))
    for j in range(m) :
        if graph[i][j] == 2 :
            virus.append((j,i))
        if graph[i][j] == 0 :
            person.append((j,i))
            
for comb in combinations(person, 3) :
    temp_grp = deepcopy(graph)
    for x,y in comb :
        temp_grp[y][x] = 1
    for i in range(n) :
        for j in range(m) :
            if temp_grp[i][j] == 2 :
                queue = deque()
                queue.append((j,i))
                while queue :
                    x,y = queue.popleft()
                    for mv in move :
                        dx = x + mv[0]
                        dy = y + mv[1]
                        if dx < 0 or dy < 0 or dx >= m or dy >= n :
                            continue
                        if temp_grp[dy][dx] == 0 :
                            queue.append((dx,dy))
                            temp_grp[dy][dx] = 2
    temp_cnt = 0
    for i in range(n) :
        temp_cnt += temp_grp[i].count(0)
    result = max(result, temp_cnt)

print(result)
                        
                
