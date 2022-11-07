import sys
from collections import defaultdict

input = sys.stdin.readline
N, K, D = map(int, input().rstrip().split())
#DP = [0] * (N+1)
boxDict = defaultdict(int)
sumValue = 0

# 각 상자에 몇개의 도토리가 있어야 하는지 대입
for _ in range(K) :
    start, end, distance = map(int, input().rstrip().split())    
    for i in range(start, end+1, distance) :
        sumValue += 1
        boxDict[i] += 1

boxes = sorted(boxDict.items())

remainder = (D % sumValue)
if remainder == 0 :
    print(boxes[-1][0])
else :
    for index, cnt in boxes :
        remainder -= cnt
        if remainder <= 0 :
            print(index)
            break
        