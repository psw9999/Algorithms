import sys
input = sys.stdin.readline

global graph, tg
N = int(input().rstrip())
graph = []
graphSum = 0

for _ in range(N) :
    temp = list(map(int, input().rstrip().split()))
    graph.append(temp)
    graphSum += sum(temp)

tg = [[0 for _ in range(N)] for _ in range(N)]
    
def division(minX, minY, maxX, maxY, divisions) :
    global graph
    sumV = 0
     
    for x in range(N) :
        for y in range(N) :
            if (x >= minX and x <= maxX) and (y >= minY and y <= maxY) :
                divisions.add((x,y))
    
    return sumV

def search(t, startX, startY, endX, endY, divisions) :
    global graph, tg
    sumV = 0
    
    for x in range(startX, endX) :
        for y in range(startY, endY) :
            if (x,y) in divisions :
                continue
            tg[x][y] = t 
            sumV += graph[x][y]
    
    return sumV
            
result = int(1e9)
for x in range(N) :
    for y in range(N) :
        for d1 in range(1, N) :
            for d2 in range(1, N) :
                if x+d1+d2 >= N or y-d1 < 0 or y+d2 >= N :
                    continue
                maxV, minV = 0, int(1e9)
                divisions = set()
                tg = [[0 for _ in range(N)] for _ in range(N)]
                values = [0,0,0,0,0]
                values[4] += division(x,y-d1,x+d1+d2,y+d2,divisions)
                if x == 1 and y == 3 and d1 == 2 and d2 == 2 : 
                    print(divisions)
                values[0] = search(1, 0,0,x+d1,y+1,divisions)
                values[1] = search(2, 0,y+1,x+d2+1,N,divisions)
                values[2] = search(3, x+d1,0,N,y-d1+d2,divisions)
                values[3] = search(4, x+d2+1,y-d1+d2,N,N,divisions)
                
                temp = graphSum - sum(values)
                values[4] += temp
                if x == 1 and y == 3 and d1 == 2 and d2 == 2 : 
                    for t in tg :
                        print(t)
                    print(values)
                minV, maxV = min(values), max(values)
                if (maxV - minV) == 17 :
                    print(x,y,d1,d2)
                result = min(result, (maxV - minV))
                
print(result)