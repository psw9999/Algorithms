import sys
from collections import defaultdict

input = sys.stdin.readline

r,c,k = map(int, input().rstrip().split())
r,c = r-1,c-1
A = []
for _ in range(3) :
    A.append(list(map(int , input().rstrip().split())))

if r < len(A) and c < len(A[0]) :
    if A[r][c] == k :
        print(0)
        exit(0)

time = 1
while time <= 100 :    
    maxV = 0
    tempList = []
    tempA = []
    # 1-1. 행 길이 >= 열의 길이
    if len(A) >= len(A[0]) :
        for i in range(len(A)) :
            tempDict = defaultdict(int)
            for j in A[i] :
                if j != 0 :
                    tempDict[j] += 1
            tempList.append(tempDict)
            maxV = max(len(tempDict.values()), maxV)
        
        # 정렬을 수행한 그래프 생성
        tempA = [[0 for _ in range((maxV * 2))] for _ in range(len(A))]
        
        for i in range(len(tempList)) :
            tempList[i] = sorted(tempList[i].items(), key = lambda item : (item[1],item[0]))
            for j in range(len(tempList[i])) :
                tempA[i][(j*2)] = tempList[i][j][0]
                tempA[i][(j*2)+1] = tempList[i][j][1]
        
    # 1-2. 행의 길이 < 열의 길이
    else :
        for j in range(len(A[0])) :
            tempDict = defaultdict(int)
            for i in range(len(A)) :
                if A[i][j] != 0 :
                    tempDict[A[i][j]] += 1
            tempList.append(tempDict)
            maxV = max(len(tempDict.values()), maxV)
        
        tempA = [[0 for _ in range(len(A[0]))] for _ in range((maxV * 2))]
        
        for j in range(len(tempList)) :
            tempList[j] = sorted(tempList[j].items(), key = lambda item : (item[1],item[0]))
            for i in range(len(tempList[j])) :
                tempA[(i*2)][j] = tempList[j][i][0]
                tempA[(i*2)+1][j] = tempList[j][i][1]

    if len(tempA) > 100 :
        A = tempA[:100]
    else :
        A = tempA

    if r < len(A) and c < len(A[0]) :
        if A[r][c] == k :
            print(time)
            exit(0)
    time += 1
    
print(-1)
