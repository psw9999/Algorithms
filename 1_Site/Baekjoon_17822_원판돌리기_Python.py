
import sys
from collections import deque
input = sys.stdin.readline
                  
N,M,T = map(int, input().rstrip().split())
circle = []

# x,y
temp = [(0,1),(1,0),(-1,0)]
 
for _ in range(N) :
    circle.append(deque(map(int, input().rstrip().split())))

for _ in range(T) :
    x,d,k = map(int, input().rstrip().split())
    for i in range(x,len(circle)+1,x) :
        if d == 0 :
            circle[i-1].rotate(k)
        else :
            circle[i-1].rotate(-k)
    
    tempL = set()
    for i in range(N) :
        for j in range(M) :
            if circle[i][j] == -1 :
                continue
            
            # queue = [(i,j,circle[i][j])]
            # while queue :
            #     y,x,target = queue.pop()
            #     for tx,ty in temp :
            #         dx = (x + tx) % M
            #         dy = y + ty
            #         if dy >= N :
            #             continue
            #         if circle[dy][dx] == target :
            #             flag = False
            #             queue.append((dy,dx,circle[dy][dx]))
            #             circle[y][x] = -1
            #             circle[dy][dx] = -1

            for tx,ty in temp :
                dx = (j + tx) % M
                dy = i + ty
                if dy >= N :
                    continue
                if circle[dy][dx] == circle[i][j] :
                    tempL.add((dy,dx))
                    tempL.add((i,j))
    
    for y,x in tempL :
        circle[y][x] = -1
    
    if not tempL :                
        total,length = 0,0
        
        for i in range(N) :
            for j in range(M) :
                if circle[i][j] != -1 :
                    total += circle[i][j]
                    length += 1
        
        if length == 0 :
            continue   
        average = total / length
        
        for i in range(N) :
            for j in range(M) :
                if circle[i][j] == -1 :
                    continue
                if average > circle[i][j] :
                    circle[i][j] += 1
                elif average < circle[i][j] :
                    circle[i][j] -= 1

        
result = 0
for i in range(N) :
    for j in range(M) :
        if circle[i][j] != -1 :
            result += circle[i][j]

print(result)
            