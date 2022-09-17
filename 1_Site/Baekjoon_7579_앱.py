
import sys

input = sys.stdin.readline
INF = int(1e9)

N,M = map(int, input().rstrip().split())
enable = list(map(int, input().rstrip().split()))
disable = list(map(int, input().rstrip().split()))
disableSum = sum(disable)

DP = [[0 for _ in range(disableSum+1)] for _ in range(N+1)]

for i in range(1, N+1) :
    for j in range(1, disableSum+1) :
        if j >= disable[i-1] :
            DP[i][j] = max(DP[i-1][j - disable[i-1]] + enable[i-1], DP[i][j])
        DP[i][j] = max(DP[i][j], DP[i-1][j])

result = INF

for dp in DP :
    print(dp)
    
for i in range(disableSum+1) :
    if DP[N][i] >= M :
        print(i)
        exit(0)