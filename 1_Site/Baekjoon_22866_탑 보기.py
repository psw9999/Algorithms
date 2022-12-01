import sys
input = sys.stdin.readline
from collections import deque
MAX = int(1e9)
N = int(input().rstrip())
buildings = list(map(int, input().rstrip().split()))
buildings = [0] + buildings
count = [[0 for _ in range(N+1)] for _ in range(2)]
near = [[MAX for _ in range(N+1)] for _ in range(2)]

# 오른쪽 방향으로 바라보기
# (높이, 위치)
queue = deque()
for i in range(N, 0, -1) :
    
    while queue :
        h,l = queue[0]
        # 우측 빌딩보다 현재 위치 빌딩이 큰 경우
        if h < buildings[i] :
            queue.popleft()
        
        # 우측 빌딩이 현재 위치 빌딩보다 큰 경우
        elif h > buildings[i] :
            count[0][i] += (count[0][l]+1)
            near[0][i] = l
            break
            
        else :
            count[0][i] = count[0][l]
            near[0][i] = near[0][l]
            break
    
    queue.appendleft((buildings[i], i))

#print(near)
# 왼쪽 방향으로 바라보기
queue = deque()
for i in range(1, N+1) :
    
    while queue :
        h,l = queue[0]
        # 우측 빌딩보다 현재 위치 빌딩이 큰 경우
        if h < buildings[i] :
            queue.popleft()
        
        # 우측 빌딩이 현재 위치 빌딩보다 큰 경우
        elif h > buildings[i] :
            count[1][i] += (count[1][l] + 1)
            near[1][i] = l
            break
        
        # 빌딩의 높이가 같은 경우
        else :
            count[1][i] = count[1][l]
            near[1][i] = near[1][l]
            break
                
    queue.appendleft((buildings[i], i))

#print(count)
for i in range(1,N+1) :
    t = count[0][i]+count[1][i]
    bef,aft = abs(near[0][i] - i), abs(near[1][i] - i)
    n = 0
    if bef < aft :
        n = near[0][i]
    else :
        n = near[1][i]
    if t != 0 :
        print("%d %d"%(t,n))
    else :
        print(0)