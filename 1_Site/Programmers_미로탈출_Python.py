from collections import deque

def solution(board):
    boardSize = len(board)
    newBoard = [[1 for _ in range(boardSize+2)] for _ in range(boardSize+2)]
    for i in range(boardSize) :
        for j in range(boardSize) :
            newBoard[i+1][j+1] = board[i][j]
    queue = deque()
    queue.append([0,1,1,2,1])
    visited = [{(1,1),(2,1)}]

    while queue :
        cost, x1, y1, x2, y2 = queue.popleft()
        # 목적지에 도달
        if (x1 == (boardSize) and y1 == (boardSize)) or (x2 == (boardSize) and y2 == (boardSize)) :
            return cost

        for t in move(newBoard,x1,y1,x2,y2) :
            tx1,ty1,tx2,ty2 = t
            if {(tx1,ty1),(tx2,ty2)} not in visited :
                queue.append([cost+1,tx1,ty1,tx2,ty2])
                visited.append({(tx1,ty1),(tx2,ty2)})

def move(newBoard,x1,y1,x2,y2) :
    move = [(1,0),(0,1),(-1,0),(0,-1)]
    rotation = [1,-1]
    temp = []

    # 상하좌우 이동
    for mx, my in move :
        dx1,dy1,dx2,dy2 = x1+mx,y1+my,x2+mx,y2+my
        if newBoard[dy1][dx1] == 0 and newBoard[dy2][dx2] == 0 :
            temp.append((dx1,dy1,dx2,dy2))

    # 수평인 경우 수직으로 회전
    if x1 == x2 :
        for r in rotation :
            if newBoard[y1][x1+r] == 0 and newBoard[y2][x2+r] == 0 :
                temp.append((x1,y1,x1+r,y1))
                temp.append((x2+r,y2,x2,y2))
    # 수직인 경우 수평으로 회전
    else :
        for r in rotation :
            if newBoard[y1+r][x1] == 0 and newBoard[y2+r][x2] == 0 :
                temp.append((x1,y1,x1,y1+r))
                temp.append((x2,y2+r,x2,y2))

    return temp