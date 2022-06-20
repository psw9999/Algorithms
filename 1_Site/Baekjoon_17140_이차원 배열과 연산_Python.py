import sys
from collections import defaultdict

input = sys.stdin.readline

r,c,k = map(int, input().rstrip().split())
r,c = r-1,c-1
A = []
for _ in range(3) :
    A.append(list(map(int , input().rstrip().split())))

def calcul(A) :
    maxV = 0
    tempList = []
    tempA = []
    for i in range(len(A)) :
        tempDict = defaultdict(int)
        for j in A[i] :
            if j != 0 :
                tempDict[j] += 1
        tempList.append(tempDict)
        maxV = max(len(tempDict.values()), maxV)    

    if maxV > 50 :
        maxV = 50
    tempA = [[0 for _ in range((maxV * 2))] for _ in range(len(A))]
    
    
    for i in range(len(tempList)) :
        tempList[i] = sorted(tempList[i].items(), key = lambda x : (x[1],x[0]))
        for j in range(len(tempList[i])) :
            tempA[i][(j*2)] = tempList[i][j][0]
            tempA[i][(j*2)+1] = tempList[i][j][1]
    
    return tempA
        

time = 0
while time <= 100 :    
    if r < len(A) and c < len(A[0]) :
        if A[r][c] == k :
            print(time)
            exit(0)
    time += 1
    # 1-1. 행 길이 >= 열의 길이
    if len(A) >= len(A[0]) :
        A = calcul(A)
        
    # 1-2. 행의 길이 < 열의 길이
    else :
        tempA = calcul(list(map(list,zip(*A))))
        A = list(map(list, zip(*tempA)))
                
print(-1)
