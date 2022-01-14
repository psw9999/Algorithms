
# import sys, string
# from collections import deque

# input = sys.stdin.readline

# R,C = map(int, input().split())

# graph = []
# alphabet = {}
# result = 0
# move = [(1,0),(-1,0),(0,1),(0,-1)]

# for i in string.ascii_uppercase :
#     alphabet[i] = 0

# for _ in range(R) :
#     graph.append(list(input().strip()))

# def dfs(x,y,cnt) :
#     global result,alphabet
#     result = max(result, cnt)
    
    
    
#     for mx,my in move :
#         dx = x + mx
#         dy = y + my
        
#         if dx < 0 or dy < 0 or dx >= C or dy >= R :
#             continue
        
#         if not alphabet[graph[dy][dx]] :
#             alphabet[graph[dy][dx]] = 1
#             dfs(dx,dy,cnt+1)
#             alphabet[graph[dy][dx]] = 0

# alphabet[graph[0][0]] = 1
# dfs(0,0,1)
# print(result)


import sys, string
from collections import deque

input = sys.stdin.readline

R,C = map(int, input().split())

graph = []
result = 1
move = [(1,0),(-1,0),(0,1),(0,-1)]

for _ in range(R) :
    graph.append(list(input().strip()))

def bfs(x,y) :
    global result
    
    queue = deque()
    queue.append((x,y,[graph[x][y]]))
    #queue = set([(x,y,graph[x][y])])
    
    while queue :
        # tx, ty, alphabet = queue.popleft()
        tx, ty, alphabet = queue.pop()
        
        for mx,my in move :
            dx = tx + mx
            dy = ty + my
        
            if dx < 0 or dy < 0 or dx >= C or dy >= R :
                continue
        
            if graph[dy][dx] not in alphabet :
                queue.append((dx,dy,alphabet+[graph[dy][dx]]))
                #3queue.add((dx,dy,alphabet+graph[dy][dx]))
                result = max(result, len(alphabet)+1)

bfs(0,0)
print(result)