import sys
from collections import deque

input = sys.stdin.readline
consulting = [(0,0)]

N = int(input().rstrip())
for _ in range(N) :
    T,P = map(int, input().rstrip().split())
    consulting.append((T, P))

dp = [0] * (N+2)
for i in range(1, N+1) :
    dp[i] = max(dp[i-1],dp[i])
    T,P = consulting[i]
    
    if (i+T) > (N+1) :
        continue
    
    dp[i+T] = max(dp[i+T], dp[i]+P)

#print(dp)
print(max(dp))