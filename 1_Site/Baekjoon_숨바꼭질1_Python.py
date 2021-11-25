
from collections import deque

n,k = map(int, input().split())
calcul = [-1,1,2]

dp = [0] * 100001

queue = deque()
queue.append(n)

while queue :
    i = queue.popleft()
    if i == k :
        print(dp[i])
        break
    for c in calcul :
        if c == 2 :
            di = i * 2
        else :
            di = i + c
        if di >= 100001 or di < 0 : 
            continue
        if dp[di] == 0 :
            dp[di] = dp[i] + 1 
            queue.append(di)

# from collections import deque 
# def bfs(): 
#     q = deque() 
#     q.append(N) 
#     while q: 
#         v = q.popleft() 
#         if v == K: 
#             print(time[v]) 
#             return 
#         for next_step in (v-1, v+1, v*2): 
#             if 0 <= next_step < MAX and not time[next_step]: 
#                 time[next_step] = time[v] + 1 
#                 q.append(next_step)
                 
# MAX = 100001 
# N, K = map(int, input().split()) 
# time = [0]*MAX 
# bfs()

