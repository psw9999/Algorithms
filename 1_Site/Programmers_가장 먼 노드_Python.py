from collections import defaultdict,deque
def solution(n, edge):
    maxV = int(1e9)
    nodes = defaultdict(list)
    for e1,e2 in edge :
        nodes[e1].append(e2)
        nodes[e2].append(e1)
    
    visited = [-1 for _ in range(n+1)]
    visited[1] = 0
    
    queue = deque()
    for n in nodes[1] :
        queue.append((n,2))
        
    while queue :
        cur,cost = queue.popleft()
        
        if visited[cur] == -1 :
            visited[cur] = cost
            for n in nodes[cur] :
                queue.append((n,cost+1))
                
        elif visited[cur] > cost :
            visited[cur] = cost
            for n in nodes[cur]  :
                queue.append((n,cost+1))
        
        else :
            continue
        
    maxC = max(visited)
    return visited.count(maxC)