from collections import deque

def ctrl_move(y,x,my,mx,tBoard) :
    dy,dx = y + my, x + mx
    if dx < 0 or dy < 0 or dx >= 4 or dy >= 4 :
        return y, x
    if tBoard[serialize(dy,dx)] == '0' :
        return ctrl_move(dy,dx,my,mx,tBoard)
    else :
        return dy,dx

def serialize(y,x) :
    return (y * 4) + x

def appendQueue(tBoard,y,x,card,cost,cnt) :
    global queue, visited, move
    
    for my,mx in move :
        dy,dx = y + my, x + mx
        if dy < 0 or dx < 0 or dx >= 4 or dy >= 4 :
            continue
        if (tBoard,dy,dx,card) not in visited :
            queue.append([tBoard,dy,dx,card,cost+1,cnt])
            visited.add((tBoard,dy,dx,card))
        ty,tx = ctrl_move(y,x,my,mx,tBoard)
        if dy == ty and dx == tx :
            continue
        if (tBoard,ty,tx,card) not in visited :
            queue.append([tBoard,ty,tx,card,cost+1,cnt])
            visited.add((tBoard,ty,tx,card))

# r : y , c : x
def solution(board, r, c):
    global queue, visited,move
    move = [(0,1),(1,0),(-1,0),(0,-1)]
    maxV = -1
    tBoard = ""
    for b in board :
        maxV = max(maxV, max(b))
        tBoard += "".join(list(map(str,b)))
    queue = deque()
    queue.append([tBoard,r,c,-1,0,maxV])
    visited = set()
    visited.add((tBoard,r,c,-1))
    
    while queue :
        tBoard,y,x,card,cost,cnt = queue.popleft()
        
        for my,mx in move :
            dy,dx = y + my, x + mx
            if dy < 0 or dx < 0 or dx >= 4 or dy >= 4 :
                continue
            if (tBoard,dy,dx,card) not in visited :
                queue.append([tBoard,dy,dx,card,cost+1,cnt])
                visited.add((tBoard,dy,dx,card))
            ty,tx = ctrl_move(y,x,my,mx,tBoard)
            if dy == ty and dx == tx :
                continue
            if (tBoard,ty,tx,card) not in visited :
                queue.append([tBoard,ty,tx,card,cost+1,cnt])
                visited.add((tBoard,ty,tx,card))
        position = serialize(y,x)
        if tBoard[position] != '0' :
            if card == -1 :
                queue.append((tBoard,y,x,position,cost+1,cnt))
            elif card != position and tBoard[card] == tBoard[position] :
                ttBoard = tBoard.replace(tBoard[card],'0')
                if (cnt-1) == 0 :
                    return cost + 1
                queue.append((ttBoard,y,x,-1,cost+1,cnt-1))