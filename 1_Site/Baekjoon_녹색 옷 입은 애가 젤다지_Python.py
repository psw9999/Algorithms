#from collections import deque

import heapq

problem_cnt = 1
move = [(0,-1),(1,0),(0,1),(-1,0)]
        
while True :
    mapSize = int(input())
    if not mapSize :
        break
    graph = []
    for _ in range(mapSize) :
        graph.append(list(map(int,input().split())))
    result = int(1e9)
    cost_map = [[result]*mapSize for _ in range(mapSize)]
    
    # 다익스트라
    queue = []
    heapq.heappush(queue, (graph[0][0],0,0))
    
    while queue :
        cost, x, y = heapq.heappop(queue)
        print (queue)
        
        if cost_map[y][x] < cost :
            continue
            
        for mx,my in move :
            dx = x + mx
            dy = y + my
            
            if dx < 0 or dy < 0 or dx >= mapSize or dy >= mapSize:
                continue
    
            d_cost = cost + graph[dy][dx]
            if d_cost < cost_map[dy][dx] :
                cost_map[dy][dx] = d_cost
                heapq.heappush(queue, (d_cost, dx, dy))
        
    print("Problem {}: {}".format(problem_cnt,cost_map[mapSize-1][mapSize-1]))
    problem_cnt+=1
    
    