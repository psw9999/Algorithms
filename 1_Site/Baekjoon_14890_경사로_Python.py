
import sys
input = sys.stdin.readline    

N,L = map(int,input().rstrip().split())
graph = []
for _ in range(N) :
    graph.append(list(map(int, input().rstrip().split())))

result = 0
for y in range(N) :
    cnt = 1
    bef = graph[y][0]
    flag = True
    ramp = False
    for x in range(1, N) :
        # 이전 블록과 현재 블록의 높이가 같은 경우
        if bef == graph[y][x] :
            cnt += 1
        # 이전 블록이 현재 블록보다 높이가 낮은 경우
        elif (bef+1) == graph[y][x] :
            if cnt < L :
                flag = False
                break
            cnt = 1
        # 이전 블록이 현재 블록보다 높이가 높은 경우
        elif bef == (graph[y][x]+1) :
            if ramp : 
                flag = False
                break
            ramp = True
            cnt = 1
        # 이전블록과 현재블록의 높이 차이가 1보다 큰 경우
        else :
            flag = False
            break
        bef = graph[y][x]
        
        if ramp and cnt >= L :
            ramp = False
            cnt -= L

    if ramp : 
        continue
    if flag :
        result += 1

for x in range(N) :
    cnt = 1
    bef = graph[0][x]
    ramp = False
    flag = True
    for y in range(1, N) :
        # 이전 블록과 현재 블록의 높이가 같은 경우
        if bef == graph[y][x] :
            cnt += 1
        # 이전 블록이 현재 블록보다 높이가 낮은 경우
        elif (bef+1) == graph[y][x] :
            if cnt < L :
                flag = False
                break
            cnt = 1
        # 이전 블록이 현재 블록보다 높이가 높은 경우
        elif bef == (graph[y][x]+1) :
            if ramp : 
                flag = False
                break
            ramp = True
            cnt = 1
        # 이전블록과 현재블록의 높이 차이가 1보다 큰 경우
        else :
            flag = False
            break
            
        if ramp and cnt >= L :
            ramp = False
            cnt -= L

        bef = graph[y][x]

    if ramp : 
        continue
    
    if flag :
        result += 1

print(result)