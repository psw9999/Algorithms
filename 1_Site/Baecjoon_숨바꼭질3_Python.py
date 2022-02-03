
# import sys
# import heapq

# input = sys.stdin.readline
# MAX = 100001
# N,K = map(int,input().rstrip().split())
# if N >= K :
#     print(N-K)
#     exit()

# queue = []
# heapq.heappush(queue,(0,N))

# visited = [-1] * MAX
# visited[N] = 0

# while queue :
#     time, loc = heapq.heappop(queue)
#     if loc == K :
#         print(time)
#         break
#     temp = 0
#     for i in range(3) :
#         if i == 0 :
#             temp = loc * 2
#         elif i == 1 :
#             temp = loc + 1
#         else :
#             temp = loc - 1
    
#         if not 0 <= temp < MAX :
#             continue
#         if visited[temp] != -1 and time >= visited[temp] :
#             continue
        
#         if i == 0:
#             heapq.heappush(queue,(time,temp))
#             visited[temp] = time
#         else :
#             heapq.heappush(queue,(time+1,temp))
#             visited[temp] = time + 1 

import sys
from collections import deque

input = sys.stdin.readline

N,K = map(int, input().rstrip().split())

MAX_V = 100000
visited = [100000] * (MAX_V+1)
queue = deque()
queue.append((N,0))
queue.append((N*2,0))
visited[N] = 0
visited[N*2] = 0

arr = [(2,0),()]

while queue :
    c,t = queue.popleft()
    
    if c == K :
        print(t)
        break
    
    temp = c*2
    if temp <= MAX_V and visited[temp] > t :
        visited[temp] = t
        queue.append((temp,t))
    
    temp = c+1
    if temp <= MAX_V and visited[temp] > t+1 :
        visited[temp] = t+1
        queue.append((temp,t+1))
    
    temp = c-1
    if 0 <= temp <= MAX_V and visited[temp] > t-1 :
        visited[temp] = t+1
        queue.append((temp,t+1))