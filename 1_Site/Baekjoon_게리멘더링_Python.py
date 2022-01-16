from itertools import combinations
from collections import deque
import sys

def search(nodeList) :
    global visited
    cnt = 0
    first = nodeList[0]
    visited[first] = True
    queue = deque()
    queue.append(first)
    while queue :
        node = queue.popleft()
        for i in graph[node] :
            if i in nodeList and visited[i] == False :
                queue.append(i)
                visited[i] = True 
    
    for i in nodeList :
        if visited[i] == False :
            return 0
        else :
            cnt += population[i]

    return cnt

input = sys.stdin.readline
N = int(input())
population = list(map(int,input().rstrip().split()))
graph = [[] for _ in range(N)]
result = int(1e9)

for i in range(N) :
    temp = list(map(int, input().rstrip().split()))
    graph[i] = temp[1:]
    for j in range(len(graph[i])) :
        graph[i][j] = graph[i][j] - 1

for i in range(1, (N//2)+1) :
    for combi in list(combinations(range(N), i)) :
        visited = [False] * N
        cnt1 = search(combi)
        if (cnt1 == 0) :
            continue   
        cnt2 = search([i for i in range(N) if i not in combi])
        if (cnt2 == 0) :
            continue
        result = min(result, abs(cnt1 - cnt2))

if result == 1e9 :
    print(-1)
else :
    print(result)
