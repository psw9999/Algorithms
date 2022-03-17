from collections import deque, defaultdict

def bfs(start,ban,nodeDict,n) :
    queue = deque([start])
    visited = [False] * (n+1)
    visited[start] = True
    visited[ban] = True
    
    cnt = 0
    while queue :
        n = queue.popleft()
        cnt += 1
        for node in nodeDict[n] :
            if visited[node] == False :
                visited[node] = True
                queue.append(node)
    return cnt

def solution(n, wires):
    nodeDict = defaultdict(list)
    result = int(1e9)
    
    for start,end in wires :
        nodeDict[start].append(end)
        nodeDict[end].append(start)
    
    for v1,v2 in wires :
        result = min(result, abs(bfs(v1,v2,nodeDict,n) - bfs(v2,v1,nodeDict,n)))
    
    return result