import heapq

def solution(n, paths, gates, summits):
    INF = int(1e9)
    result = [0, INF]
    graph = [[] for _ in range(n+1)]
    
    for i,j,w in paths :
        graph[i].append((j,w))
        graph[j].append((i,w))
    
    queue = []
    distances = [INF] * (n+1)
    for gate in gates :
        distances[gate] = 0
        heapq.heappush(queue, (0, gate))
        
    while queue :
        distance, node = heapq.heappop(queue)
        
        if distance > distances[node] :
            continue
        
        if node in summits :
            if distance < result[1] :
                result = [node, distance]
                
            elif distance == result[1] :
                if node < result[0] :
                    result[0] = node
            continue
        
        for n,d in graph[node] :
            temp = max(distance, d)
            if distances[n] > temp :
                distances[n] = temp
                heapq.heappush(queue, (temp, n))
    
    return result
        
    
    
    