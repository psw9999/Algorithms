
import sys

input = sys.stdin.readline
move = [(0,0),(-1,0),(1,0),(0,1),(0,-1)]

R,C,M = map(int,input().rstrip().split())
graph = [[[None] for _ in range(C)] for _ in range(R)]

shark = []

for i in range(M) :
    temp = list(map(int,input().rstrip().split()))
    temp[0]-=1
    temp[1]-=1
    # if temp[0] == 0 and temp[3] == 1 :
    #     temp[3] = 2
    # elif temp[0] == (R-1) and temp[3] == 2 :
    #     temp[3] = 1
    # elif temp[1] == (C-1) and temp[3] == 3 :
    #     temp[3] = 4
    # elif temp[1] == 0 and temp[3] == 4 :
    #     temp[3] = 3
            
    shark.append(temp)
    y,x = shark[i][0],shark[i][1]
    graph[y][x] = [i]

result = 0 
for loc in range(C) :
#for loc in range(1) :   
    # 현재 열의 상어 체크
    for ver in range(R) :
        if graph[ver][loc] != [None] :
            ts = graph[ver][loc].pop()
            result += shark[ts][4]
            # 잡은 상어 삭제
            shark[ts] = None
            graph[ver][loc] = [None]
            break
    
    # 상어 이동
    for i in range(M) :
        # 잡히거나 먹힌 상어라면 이동 x
        if shark[i] == None :
            continue
        
        r,c,s,d,z = shark[i][0],shark[i][1],shark[i][2],shark[i][3],shark[i][4]
        
        if r == 0 and d == 1 :
            d = 2
        elif r == (R-1) and d == 2 :
            d = 1
        elif c == (C-1) and d == 3 :
            d = 4
        elif c == 0 and d == 4 :
            d = 3
        
        if s == 0 :
            continue
        
        graph[r][c].remove(i)
        if len(graph[r][c]) == 0 :
            graph[r][c] = [None]
        tr,tc = r,c
        
        # 상
        if d == 1 :
            tr = r - s
            if tr <= 0 :
                tr = abs(tr)
                if ((tr // (R-1)) % 2) == 1 :
                    tr = (R-1)- tr%(R-1)
                    d = 1
                else :
                    tr = tr%(R-1)
                    d = 2
        
        # 하
        elif d == 2 :
            tr = r + s
            if tr >= (R-1) :
                if ((tr // (R-1)) % 2) == 1 :
                    tr = (R-1)- tr%(R-1)
                    d = 1
                else :
                    tr = tr%(R-1)
                    d = 2
                
                                
        # 우
        elif d == 3 :
            tc = c + s
            if tc >= (C-1) :
                if ((tc // (C-1)) % 2) == 1 :
                    tc = (C-1) - tc%(C-1)
                    d = 4
                else :
                    tc = tc%(C-1)
                    d = 3          
                
        # 좌 
        elif d == 4 :
            tc = c - s
            if tc <= 0 :
                tc = abs(tc)
                if ((tc // (C-1)) % 2) == 1 :
                    tc = (C-1) - tc%(C-1)
                    d = 4
                else :
                    tc = tc%(C-1)
                    d = 3            
            
        
        shark[i][0],shark[i][1],shark[i][2],shark[i][3],shark[i][4] = tr,tc,s,d,z
        
        # 상어 추가
        print(r,c,s,tr,tc)
        if graph[tr][tc] == [None] :
            graph[tr][tc] = [i]
            
        else :
            graph[tr][tc].append(i)

    # 같은 칸의 상어 잡아먹기
    for y in range(R) :
        for x in range(C) :
            if len(graph[y][x]) >= 2 :
                #print(y,x)
                maxV, max_index = 0,-1
                for index in graph[y][x] :
                    temp,temp_index = shark[index][4],index
                    if maxV < temp :
                        maxV = temp
                        max_index = temp_index
                    
                for index in graph[y][x] :
                    if index != max_index :
                        shark[index] = None
                
                graph[y][x] = [max_index]
    

print(result)    
                
