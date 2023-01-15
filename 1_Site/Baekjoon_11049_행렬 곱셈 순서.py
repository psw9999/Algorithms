import sys
input = sys.stdin.readline

MAX = int(2e31) - 1
N = int(input())
matrixs = []
for _ in range(N) :
    r,c = map(int, input().rstrip().split())
    matrixs.append((r,c))

dp = [[MAX for _ in range(N)] for _ in range(N)]
for i in range(N) :
    dp[i][i] = 0

# 몇번째 대각선?
for i in range(1, N) :
    for j in range(N-i) :
        
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + nums[i]*nums[k+1]*nums[j+1])
        
print(dp[0][-1])
