from collections import deque

def solution(m, n, board):
    global move, graph, removeList
    move = [(1,0),(0,1),(1,1)]
    graph = [list(board[i]) for i in range(m)]
    removeList = deque()
    result = 0 
    
    while True :
        for i in range(m-1) :
            for j in range(n-1) :
                if graph[i][j] != 0 :
                    blockCheck(j,i,graph[i][j])
                
        if not removeList :
            break
        
        # 블록 삭제
        while removeList :
            y,x = removeList.popleft()
            if graph[y][x] != 0 :
                graph[y][x] = 0
                result += 1
        
        # 블록 아래로 내리기
        for i in range(m-2,-1,-1) :
            for j in range(n) :
                if graph[i][j] != 0 :
                    temp = blankCheck(j,i,m)
                    if temp != i :
                        graph[temp][j] = graph[i][j]
                        graph[i][j] = 0
                 
    return result
        
def blockCheck(x,y,friends) :
    global move, graph, removeList
    for mx,my in move :
        dx,dy = x+mx, y+my
        if graph[dy][dx] != friends :
            return
    
    removeList.append((y,x))
    for mx, my in move :
        dx,dy = x+mx, y+my
        removeList.append((dy,dx))

def blankCheck(x,y,m) :
    global graph
    
    if graph[y+1][x] == 0 :
        if (y+1) == (m-1) :
            return y+1
        return blankCheck(x,y+1,m)
        
    else :
        return y