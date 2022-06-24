from re import L
import sys

input = sys.stdin.readline
N = int(input().rstrip())
triangle = []
DP = []
for i in range(N) :
    triangle.append(list(map(int, input().rstrip().split())))
    DP.append([0 for _ in range(i+1)])
DP[0][0] = triangle[0][0]

for i in range(N-1) :
    for j in range(len(DP[i])) :
        DP[i+1][j] = max(DP[i+1][j], DP[i][j] + triangle[i+1][j])
        DP[i+1][j+1] = max(DP[i+1][j+1], DP[i][j] + triangle[i+1][j+1])

print(max(DP[N-1]))

