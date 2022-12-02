import sys
input = sys.stdin.readline
from collections import deque, defaultdict

move = [(1,0), (-1,0), (0,1), (0,-1)]

puzzle = ""
for _ in range(3) :
    a,b,c = map(str, input().rstrip().split())
    puzzle += (a+b+c)

def bfs() :
    queue = deque()
    queue.append((puzzle,0))
    
    visited = defaultdict(bool)
    target = "123456780"
    
    while queue :
        cur,count = queue.popleft()
        if cur == target :
            print(count)
            return
        empty = cur.find("0")
        x,y = empty // 3, empty % 3
        
        for mx,my in move :
            dx,dy = x + mx, y + my
            
            if dx < 0 or dy < 0 or dx >= 3 or dy >= 3 :
                continue
            index = (dx*3)+dy
            temp = list(cur)
            temp[empty] = temp[index]
            temp[index] = "0"
            temp = ''.join(temp)
            if visited[temp] :
                continue
            else :
                visited[temp] = True
            queue.append((temp, count+1))

    print(-1)

bfs()