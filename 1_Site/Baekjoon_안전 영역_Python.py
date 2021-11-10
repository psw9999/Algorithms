
import sys
sys.setrecursionlimit(10**6)
def input(): return sys.stdin.readline()

n = int(input())

maxHgt = 0
move = [(1,0),(-1,0),(0,1),(0,-1)]

array = [[0] * n for i in range(n)]

result = 0

for i in range(n) :
    array[i] = list(map(int,input().split()))
    maxHgt = max(maxHgt, max(array[i]))

for i in range(0, maxHgt) :
    tempResult = 0
    tempArray = [[0] * n for i in range(n)]
    stack = []
    # 해당 부분때문에 오래 걸림. 두번 리스트를 작성하기 때문에..
    for y in range(n) :
        for x in range(n) :
            if array[y][x] > i :
                tempArray[y][x] = 1
    
    for y in range(n) :
        for x in range(n) :
            if tempArray[y][x] == 1:
                tempResult+=1
                stack.append((x,y))
                while stack :
                    tx,ty = stack.pop()
                    if tx < 0 or ty < 0 or tx > (n-1) or ty > (n-1) :
                        continue
                    if tempArray[ty][tx] == 0 :
                        continue
                    if tempArray[ty][tx] == 1 :
                        tempArray[ty][tx] = 0
                        for m in move :
                            stack.append((tx+m[0],ty+m[1]))

    result = max(result, tempResult)

print(result)
    
