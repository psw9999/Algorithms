
import sys
input = sys.stdin.readline
move = [(1,0),(0,-1),(-1,0),(0,1)]

N = int(input())
graph = [[0] * 101 for _ in range(101)]

def location(x,y) :
    if y == -1 :
        return (-1,0)
    elif y == 1 :
        return (1,0)
    elif x == -1 :
        return (0,1)
    else :
        return (0,-1) 
    
for _ in range(N) :
    x,y,mv,curve = map(int,input().rstrip().split())
    graph[y][x] = 1
    #cur = (x+move[mv][0], y+move[mv][1])
    x,y = x+move[mv][0],y+move[mv][1]
    graph[y][x] = 1
    move_list = [(move[mv][0],move[mv][1])]
    
    for i in range(curve) :
        # if i == 0 :
        #     temp = (move_list[0][1],(-move_list[0][0]))
        #     move_list.append(temp)
        #     #cur = (cur[0] + temp[0], cur[1] + temp[1])
        #     x,y = x+temp[0], y+temp[1]
        #     graph[y][x] = 1
        # else :
        for j in range(len(move_list)-1,-1,-1) :
            dx,dy = location(move_list[j][0], move_list[j][1])
            x = x + dx
            y = y + dy
            move_list.append((dx,dy))
            graph[y][x] = 1
    
    #print(move_list)

result = 0
for y in range(len(graph)-1) :
    for x in range(len(graph)-1) :
        if graph[y][x] and graph[y+1][x] and graph[y][x+1] and graph[y+1][x+1] :
            result += 1                
print(result)