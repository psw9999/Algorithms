def solution(m, n, puddles):
    move = [(0,1),(1,0)]
    maxV = int(1e9)
    graph = [[[0,maxV] for _ in range(m)] for _ in range(n)]
    
    graph[0][0] = [1,0]
    
    for px,py in puddles :
        graph[py-1][px-1] = [-1,0]
    
    
    for y in range(len(graph)) :
        for x in range(len(graph[0])) :
            if graph[y][x][0] == -1 :
                continue
            for mx,my in move :
                dx,dy = x + mx, y + my
                if dy == n or dx == m :
                    continue
                if graph[dy][dx][0] == -1 :
                    continue
                # 비용이 같으면, 경우의 수를 더해줌.
                if (graph[y][x][1]+1) == graph[dy][dx][1] :
                    graph[dy][dx][0] += graph[y][x][0]
                # 비용이 더 작으면, 경우의 수를 이전 값으로 초기화
                elif (graph[y][x][1]+1) < graph[dy][dx][1] : 
                    graph[dy][dx][1] = graph[y][x][1]+1
                    graph[dy][dx][0] = graph[y][x][0]
    
    return (graph[n-1][m-1][0] % 1000000007)