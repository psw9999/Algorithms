
import sys
input = sys.stdin.readline

dir = [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1)]
N,M,K = map(int,input().rstrip().split())
graph = []
for i in range (N) :
    graph.append([])
    for _ in range(N) :
        graph[i].append([])
for g in graph :
    print(g)

queue = []

for _ in range(M) :
    r,c,m,s,d = map(int,input().rstrip().split())
    queue.append((r-1,c-1,m,s,d))


for _ in range(K) :
    while queue :
        y,x,m,s,d = queue.pop(0)
        
        my,mx = dir[d][1] * s, dir[d][0] * s
        dy,dx = (my + y) % N, (mx + x) % N
        graph[dy][dx].append((m,s,d))
    
    for i in range(N) :
        for j in range(N) :
            Fcount = len(graph[i][j])
            if Fcount > 1 :
                tm,ts,td = 0,0,-1
                flag = True
                while graph[i][j] :
                    dm,ds,dd = graph[i][j].pop()
                    tm += dm
                    ts += ds
                    if flag :
                        if td != -1 and (dd%2) != td:
                            flag = False
                    td = (dd%2)
                    
                tm //= 5
                ts //= Fcount 
                if not tm :
                    continue
                
                if flag :
                    td = [0,2,4,6]
                else :
                    td = [1,3,5,7]
                
                for ttd in td :
                    # tx = (j + dir[ttd][0]) % N
                    # ty = (i + dir[ttd][1]) % N
                    queue.append((i,j,tm,ts,ttd))
                    
            elif Fcount == 1 :
                dm,ds,dd = graph[i][j].pop()
                queue.append((i,j,dm,ds,dd))
    
result = 0
for y,x,m,s,d in queue :
    result += m

print(result)