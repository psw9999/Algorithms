
N = int(input())

move = [(0,0),(1,0),(-1,0),(0,1),(0,-1)]

graph = []
for _ in range(N) :
    graph.append(list(map(int, input().split())))

Tgraph = [[0] * N for _ in range(N)]
for y in range(1,N-1) :
    for x in range(1,N-1) :
        for mv in move :
            dx = x + mv[0]
            dy = y + mv[1]
            Tgraph[y][x] += graph[dy][dx]

result = 3000
visited = [[0] * N for _ in range(N)]

def check(x,y) :
    for mx, my in move :
        dx = x + mx
        dy = y + my
        if dx < 0 or dy < 0 or dx >= N or dy >= N or visited[dy][dx] :
            return False
    return True

def search(tx, ty, cnt, value) :
    global result
    if cnt == 3 :
        result = min(result, value)
        return 
    for y in range(ty, N) :
        for x in range(tx, N) :
            if check(x,y) :
                for mx, my in move :
                    dx = x + mx
                    dy = y + my
                    visited[dy][dx] = 1
                value += Tgraph[y][x]
                search(x,y,cnt+1,value)
                
                value -= Tgraph[y][x]
                for mx, my in move :
                    dx = mx + x
                    dy = my + y
                    visited[dy][dx] = 0

search(1,1,0,0)
print(result)
                