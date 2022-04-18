
import sys
input = sys.stdin.readline

N = int(input())
DP = [[0 for _ in range(3)] for _ in range(N)]
home = []
result = int(1e9)

for _ in range(N) :
    temp = list(map(int, input().rstrip().split()))
    home.append(temp)

DP[0] = home[0]
for i in range(1, N) :
    for j in range(3) :
        #DP[i][j] = DP[i-1][j] + min(home[i][(j+1)%3], home[i][(j+2)%3])
        DP[i][j] = home[i][j] + min(DP[i-1][(j+1)%3], DP[i-1][(j+2)%3])

print(min(DP[N-1]))