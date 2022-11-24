    import sys
    from itertools import combinations
    from collections import deque

    global graph
    input = sys.stdin.readline
    move = [(1,0),(0,1),(-1,0),(0,-1)]
    loc = [(x,y) for x in range(5) for y in range(5)]
    combs = combinations(loc,7)

    # 그래프 입력받기
    graph = []
    for _ in range(5) :
        graph.append(list(input().rstrip()))

    # 이어져있는지 확인하는 그래프
    visited = [[0 for _ in range(5)] for _ in range(5)]

    def checkY(comb) :
        global graph
        
        Ycnt = 0
        for (x,y) in comb :
            if graph[x][y] == 'Y' :
                Ycnt += 1
        
        if Ycnt >= 4 :
            return False
        else :
            return True

    def checkGraph(comb) :
        cnt = 1
        for (x,y) in comb :
            visited[x][y] = 1
        
        v = [comb[0]]
        queue = deque()
        queue.append(comb[0])
        while queue :
            (x,y) = queue.popleft()
            for mx,my in move :
                dx,dy = x+mx, y+my
                if dx < 0 or dy < 0 or dx >= 5 or dy >= 5 :
                    continue
                if visited[dx][dy] == 1 and (dx,dy) not in v :
                    queue.append((dx,dy))
                    v.append((dx,dy))
                    cnt += 1
        
        for (x,y) in comb :
            visited[x][y] = 0
        
        if cnt >= 7 :
            return True
        else :
            return False
                
    # 조합 돌아보며 확인
    result = 0
    for comb in combs :
        if checkY(comb) and checkGraph(comb) :
            result += 1

    print(result) 
            
            