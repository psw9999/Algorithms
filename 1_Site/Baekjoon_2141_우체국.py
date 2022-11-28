
import sys
from collections import defaultdict

input = sys.stdin.readline

X = defaultdict(int)
N = int(input().rstrip())
left, right = int(1e9), int(-1e9)

for _ in range(N) :
    x,a = map(int, input().rstrip().split())
    left = min(left, x)
    right = max(right, x)
    X[x] = a

towns = sorted(X.items(), key = lambda x: x[0])

# 이진탐색
result, resultV = right, int(1e28) + 1
while left <= right :
    mid = (left + right) // 2
    temp = 0
    l,r = 0,0
    for i in range(N) :
        x,a = towns[i]
        if mid >= x :
            temp += ((mid - x) * a)
            l += ((mid - x) * a)
        else :
            temp += ((x - mid) * a)
            r += ((x - mid) * a)
    
    if temp < resultV :
        resultV = temp
        result = mid
    elif temp == resultV :
        result = min(result, mid)
    
    if l > r :
        right = mid - 1
    else :
        left = mid + 1
    
print(result)
        
