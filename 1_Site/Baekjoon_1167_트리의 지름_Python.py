
import sys
from collections import deque, defaultdict
input = sys.stdin.readline

V = int(input())
dict = defaultdict(list)
for _ in range(V) :
    temp = list(map(int,input().rstrip().split()))[:-1]
    cur = temp[0]
    for i in range(1,len(temp),2) :
        dict[cur].append((temp[i],temp[i+1]))
        dict[temp[i]].append((cur,temp[i+1]))

# 처음 순회 (가장 하위 노드 찾기)
queue = deque()
visited = [False] * (V+1)
visited[1] = True
temp = 0
lastNode = -1
for node, distance in dict[1] :
    queue.append((node,distance))
    visited[node] = True
while queue :
    node,distance = queue.popleft()
    if temp < distance :
        lastNode = node
        temp = distance
    for tNode, tDistance in dict[node] :
        if visited[tNode] == False :
            queue.append((tNode, distance + tDistance))
            visited[tNode] = True

# 말단 노드부터 끝 노드까지 bfs 진행
visited = [False] * (V+1)
visited[lastNode] = True
result = 0
for node,distance in dict[lastNode] :
    queue.append((node,distance))
    visited[node] = True
while queue :
    node,distance = queue.popleft()
    result = max(result, distance)
    for tNode, tDistance in dict[node] :
        if visited[tNode] == False :
            queue.append((tNode, distance + tDistance))
            visited[tNode] = True

print(result)
    
    