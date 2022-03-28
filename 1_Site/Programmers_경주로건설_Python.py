from collections import deque
def solution(board):
    move = [(0,-1),(-1,0),(0,1),(1,0)]
    maxV = int(1e9)
    visited = [[[maxV for _ in range(len(board[0]))] for _ in range(len(board))] for _ in range(4)]
    for i in range(4) :
        visited[i][0][0] = 0
    
    queue = deque()
    if board[0][1] == 0 :
        queue.append((1,0,3))
        #visited[0][1] = 100
        visited[3][0][1] = 100
    if board[1][0] == 0 :
        queue.append((0,1,2))
        #visited[1][0] = 100
        visited[2][1][0] = 100
    
    #queue.append((0,0,0))
    #queue.append((0,0,2))
    
    result = maxV
    while queue :
        x,y,direct = queue.popleft()
        
        if result <= visited[direct][y][x] :
            continue
        
        if x == (len(board)-1) and y == (len(board)-1) :
            result = min(result, visited[direct][y][x])
            continue
        
        for i,(mx,my) in enumerate(move) :
            dx,dy = x+mx, y+my
            
            if move[direct][0] == (mx * -1) and move[direct][1] == (my * -1) :
                continue
            
            if dx < 0 or dy < 0 or dx >= len(board) or dy >= len(board) or board[dy][dx] == 1  :
                continue
                
            temp = 0
            if move[direct][0] == mx and move[direct][1] == my :
                temp = visited[direct][y][x] + 100
            else :
                temp = visited[direct][y][x] + 600
            
            # 같은 방향의 DP만 체크
            # if temp <= visited[i][dy][dx] :
            #     visited[i][dy][dx] = temp
            #     queue.append((dx,dy,i))
            
            # 다른 방향의 DP의 값도 체크하여 이것보다 크면 전개 안함.
            flag = True
            for j in range(4) :
                if temp-400 > visited[j][dy][dx] :
                    flag = False
                    break
            
            if flag :
                visited[i][dy][dx] = temp
                queue.append((dx,dy,i))
    
    
    return result