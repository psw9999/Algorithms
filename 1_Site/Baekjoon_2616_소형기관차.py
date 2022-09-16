
import sys

input = sys.stdin.readline

N = int(input())
clients = list(map(int, input().rstrip().split()))
S = [0]
for i in range(len(clients)) :
    S.append(S[i] + clients[i])
limit = int(input())

DP = [[0 for _ in range(N+1)] for _ in range(4)]

for i in range(1, len(DP)) :
    for j in range((limit * i), len(DP[i])) :
        DP[i][j] = max(DP[i][j-1], DP[i-1][j-limit] + (S[j] - S[j - limit]))

print(DP[3][N])