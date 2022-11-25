import sys
from collections import deque
input = sys.stdin.readline

N,C = map(int, input().rstrip().split())
M = int(input().rstrip())

# 패키지 입력 받기
packages = []
for _ in range(M) :
    s,e,w = map(int, input().rstrip().split())
    packages.append((s,e,w))

# 패키지 정렬
packages.sort(key = lambda x: (x[1]), reverse=True)

towns = [0] * (N+1)
result = 0
while packages :
    start, end, weight = packages.pop()
    
    possibleWeight = min(C - max(towns[start:end]), weight)
    result += possibleWeight
    for i in range(start, end) :
        towns[i] += possibleWeight

print(result)