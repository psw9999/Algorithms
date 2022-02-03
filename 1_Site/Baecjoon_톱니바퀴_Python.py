
import sys
from collections import deque
input = sys.stdin.readline

gear = []

# 정방향
def direction(num) :
    global gear,visited
    # if num < 0 or num > 3 :
    #     return
    visited[num] = True
    if num < 3 and visited[num+1] == False :
        if gear[num][2] != gear[num+1][6] :
            opposite(num+1)
    if num > 0 and visited[num-1] == False :
        if gear[num][6] != gear[num-1][2] :
            opposite(num-1)            
    gear[num].appendleft(gear[num].pop())
    
# 역방향
def opposite(num) :
    global gear, visited
    # if num < 0 or num > 3 :
    #     return
    visited[num] = True
    if num < 3 and visited[num+1] == False :
        if gear[num][2] != gear[num+1][6] :
            direction(num+1)            
    if num > 0 and visited[num-1] == False :
        if gear[num][6] != gear[num-1][2] :
            direction(num-1)    
    gear[num].append(gear[num].popleft())

for _ in range(4) :
    temp = list(map(int,input().rstrip()))
    gear.append(deque(temp))

N = int(input())

for _ in range(N) :
    n, dir = map(int, input().rstrip().split())
    n = n - 1
    visited = [False] * 4
    if dir == 1:
        direction(n)
    else :
        opposite(n)
    
result = (gear[0].popleft()) + ((gear[1].popleft() * 2)) + ((gear[2].popleft() * 4)) + ((gear[3].popleft() * 8))

print(result)