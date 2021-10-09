# bfs 풀이방법
from collections import deque

#dfs
def solution(maps):
    f_x,f_y = len(maps[0])-1,len(maps)-1
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    result = -1
    
    #이렇게 하면 x,y로 꺼낼 수가 없다.
    #deque_map = deque((0,0))
    deque_map = deque()
    deque_map.append((0,0))
    maps[0][0] = 2
    
    # 큐가 빌때까지 진행
    while deque_map : 
        x,y = deque_map.popleft()
        
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx > f_x or ny > f_y :
                continue
            
            if maps[ny][nx] == 0 :
                continue
            
            if maps[ny][nx] == 1 :
                maps[ny][nx] = maps[y][x]+1
                deque_map.append((nx,ny)) 
                
    if (maps[f_y][f_x] == 1) :
        maps[f_y][f_x] = 0
    
    return maps[f_y][f_x]-1


# dfs 풀이방법
# def dfs(maps,x,y,f_x,f_y,expense) :
    
#     if x == f_x and y == f_y :
#         return expense
    
#     if x >= 0 and y >= 0 and x <= f_x and y <= f_y and (maps[y][x] == 1 or maps[y][x] > expense):
#         maps[y][x] = expense + 1
#         result = min([
#             dfs(maps,x-1,y,f_x,f_y,expense+1),
#             dfs(maps,x+1,y,f_x,f_y,expense+1),
#             dfs(maps,x,y+1,f_x,f_y,expense+1),
#             dfs(maps,x,y-1,f_x,f_y,expense+1),
#         ])
#         return result
        
#     else :
#         return 100000
    
# def solution(maps):
#     f_x,f_y = len(maps[0])-1,len(maps)-1
#     for 
#     result = dfs(maps,0,0,f_x,f_y,1)
#     if(result == 100000) :
#         return -1
    
#     return result
        
       
