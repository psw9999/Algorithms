from collections import deque

n,m,k = map(int, input().split())

graph = [[0]*m for _ in range(n)]

move = [(1,0),(-1,0),(0,1),(0,-1)]

result = []

for _ in range(k) :
    lx,ly,hx,hy = map(int, input().split())
    for i in range(n-hy, n-ly) :
        for j in range(lx, hx) :
            graph[i][j] = 1
            
for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 0 :
            queue = deque()
            queue.append((j,i))
            graph[i][j] = 1
            area = 1
            while queue :
                x,y = queue.popleft()
                for mv in move :
                    dx = x + mv[0]
                    dy = y + mv[1]
                    if dx < 0 or dy < 0 or dx >= m or dy >= n : 
                        continue
                    if graph[dy][dx] == 0 :
                        area += 1
                        graph[dy][dx] = 1
                        queue.append((dx,dy))
            result.append(area)

print(len(result))
result.sort()
for r in result :
    print(r, end = ' ')
                    