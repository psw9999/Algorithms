import heapq

def dijkstra(start,a,b,n) :
    global graph
    distance = [maxV] * (n+1)
    queue = []
    heapq.heappush(queue,(0,start))
    distance[start] = 0

    while queue :
        dist, cur = heapq.heappop(queue)

        if distance[cur] < dist :
            continue

        for i in graph[cur] :
            cost = dist + i[1]

            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(queue,(cost,i[0]))

    return distance


def solution(n, s, a, b, fares):
    global distance, graph, maxV
    maxV = int(1e9)
    graph = [[] for _ in range(n+1)]

    for start, end, fare in fares :
        graph[end].append((start,fare))
        graph[start].append((end, fare))

    distance = dijkstra(s,a,b,n)
    result = distance[a] + distance[b]

    for i in range(1, n+1) :
        if i == s :
            continue
        temp = dijkstra(i,a,b,n)
        result = min(result, distance[i] + temp[a] + temp[b])

    return result