
import sys

input = sys.stdin.readline

N,M,L,K = map(int,input().rstrip().split())
stars = []
for _ in range(K) :
    x,y = map(int,input().rstrip().split())
    stars.append((x,y))

result = 0
for i in range(len(stars)) :
    sx = stars[i][0]
    ex = sx + L
    for j in range(len(stars)) :
        sy = stars[j][1]
        ey = sy + L
        temp = 0
        for x,y in stars :
            if sx <= x <= ex :
                if sy <= y <= ey :
                    temp += 1
        result = max(result, temp)

print(len(stars)-result)    

