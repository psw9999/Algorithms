from collections import deque

N = int(input())
graph = [[0] * (N) for _ in range(N)]

K = int(input())
move = [(1,0),(0,1),(-1,0),(0,-1)]

for _ in range(K) :
    y,x = map(int,input().split())
    graph[y-1][x-1] = 1
    
L = int(input())
command = []
for _ in range(L) :
    t, Tdir = map(str, input().split())
    command.append((int(t),Tdir))
    
snake = deque()
snake.append((0,0))

dx = 0
dy = 0
dir = 0
time = 0
while True :
    time += 1
    dx += move[dir][0]
    dy += move[dir][1]
    
    if (dx,dy) in snake :
        break

    if dx < 0 or dy < 0 or dx >= N or dy >= N :
        break
    
    else :
        if graph[dy][dx] == 1:
            graph[dy][dx] = 0
            snake.append((dx,dy))
        else :
            snake.append((dx,dy))
            snake.popleft()
            
    for c in command :
        if time == c[0] :
            command.remove(command[0])
            if c[1] == 'D' :
                dir = (dir + 1) % 4
            else :
                dir = (dir - 1) % 4
        break
   
print(time)