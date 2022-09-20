
import sys

input = sys.stdin.readline

N,K = map(int,input().rstrip().split())
transport = [[]]
DP = [[0 for _ in range(K+1)] for _ in range(N+1)]
for _ in range(N) :
    transport.append(list(map(int,input().rstrip().split())))

DP[1][transport[1][0]] = transport[1][1]
DP[1][transport[1][2]] = max(DP[1][transport[1][2]], transport[1][3])

for i in range(2, N+1) :
    for j in range(K+1) :
        if DP[i-1][j] == 0 :
            continue
        
        if (j + transport[i][0]) <= K :
            DP[i][j + transport[i][0]] = max(DP[i][j + transport[i][0]], DP[i-1][j] + transport[i][1])
 
        if (j + transport[i][2]) <= K :
            DP[i][j + transport[i][2]] = max(DP[i][j + transport[i][2]], DP[i-1][j] + transport[i][3])

print(max(DP[N]))