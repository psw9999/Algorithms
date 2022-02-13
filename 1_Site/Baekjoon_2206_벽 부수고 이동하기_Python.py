
import sys
from collections import deque
input = sys.stdin.readline
move = [(1,0),(0,1),(-1,0),(0,-1)]
N,M = map(int,input().rstrip().split())

graph = []
visited_bef = [[False for _ in range (M)] for _ in range(N)]
visited_aft = [[False for _ in range (M)] for _ in range(N)]
for _ in range(N) :
    graph.append(list(input().rstrip()))

queue = deque()
queue.append((0,0,1,False))
visited_bef[0][0] = True

while queue :
    x,y,cnt,breaked = queue.popleft()
    #print(x,y)
    
    if x == (M-1) and y == (N-1) :
        print(cnt)
        exit(0)
    
    
    for mx,my in move :
        dx,dy = x + mx, y + my
        if dx < 0 or dy < 0 or dy >= N or dx >= M :
            continue
        if not breaked :
            if graph[dy][dx] == '0' and visited_bef[dy][dx] == False :
                visited_bef[dy][dx] = True
                queue.append((dx,dy,cnt+1,False))
            if graph[dy][dx] == '1' and visited_aft[dy][dx] == False :
                visited_aft[dy][dx] = True
                queue.append((dx,dy,cnt+1,True))
        else :
            if graph[dy][dx] == '0' and visited_bef[dy][dx] == False and visited_aft[dy][dx] == False :
                visited_aft[dy][dx] = True
                queue.append((dx,dy,cnt+1,True)) 

print(-1)