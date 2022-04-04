

def solution(rows, columns, queries):
    graph = [[i+1+(j*columns) for i in range(columns)] for j in range(rows)]
    result = []
    
    for y1,x1,y2,x2 in queries :
        x1,y1,x2,y2 = x1-1, y1-1, x2-1, y2-1
        
        temp = graph[y1][x1]
        minV = temp
        #상단 이동
        for i in range(x1,x2) :
            temp2 = graph[y1][i+1]
            graph[y1][i+1] = temp
            temp = temp2
            minV = min(minV, temp)
        
        # 우측 이동
        for i in range(y1,y2) :
            temp2 = graph[i+1][x2]
            graph[i+1][x2] = temp
            temp = temp2
            minV = min(minV, temp)
        
        # 하단 이동
        for i in range(x2,x1,-1) :
            temp2 = graph[y2][i-1]
            graph[y2][i-1] = temp
            temp = temp2
            minV = min(minV, temp)
        
        # 좌측 이동
        for i in range(y2,y1,-1) :
            temp2 = graph[i-1][x1]
            graph[i-1][x1] = temp
            temp = temp2
            minV = min(minV, temp)
        
        result.append(minV)
    
    return result

            