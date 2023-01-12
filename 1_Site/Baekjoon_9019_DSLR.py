import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

def D (number) :
    return (number * 2) % 10000

def S (number) :
    temp = number - 1
    if temp < 0 :
        return 9999
    return temp

def L (number) :
    return ((number % 1000) * 10) + (number // 1000)

def R (number) :
    return (number // 10) + ((number % 10) * 1000)


for _ in range(T) :
    start, target = map(int, input().rstrip().split())
    visited = [False] * 10000
    visited[start] = True
    queue = deque()
    queue.append((start, ""))
    
    while queue :
        number, reg = queue.popleft()
        
        if number == target :
            print(reg)
            break
        
        temp = D(number)
        if not visited[temp] :
            visited[temp] = True
            queue.append((temp, reg+"D"))
        temp = S(number)
        if not visited[temp] :
            visited[temp] = True
            queue.append((temp, reg+"S"))
        temp = L(number)
        if not visited[temp] :
            visited[temp] = True
            queue.append((temp, reg+"L"))
        temp = R(number)
        if not visited[temp] :
            visited[temp] = True
            queue.append((temp, reg+"R"))
    