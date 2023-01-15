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

for i in range(1, N) :
    for start in range(N-i) :
        end = start+i        
        for k in range(start, end):
            dp[start][end] = min(dp[start][end], dp[start][k] + dp[k+1][end] + (matrixs[start][0] * matrixs[k][1] * matrixs[end][1]))

print(dp[0][-1])
