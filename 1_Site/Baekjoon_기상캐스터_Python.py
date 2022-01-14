
H,W = map(int, input().split())

graph = []
result = [[-1] * W for _ in range(H)]

for _ in range(H) :
    graph.append(list(input()))

for i in range(H) :
    cnt = -1 
    for j in range(W) :
        if graph[i][j] == 'c' :
            cnt = 0
            result[i][j] = cnt
        else :
            if cnt >= 0 :
                cnt+=1
                result[i][j] = cnt
          
for res in result :
    for r in res :
        print(r, end=' ')
    print()