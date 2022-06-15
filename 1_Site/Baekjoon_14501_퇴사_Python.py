import sys

input = sys.stdin.readline

N = int(input())
DP = [0] * (N+2)
work = [(0,0)]
for _ in range(N) :
    T,P = map(int, input().rstrip().split())
    work.append((T,P))
work.append((0,0))

result = 0
for i in range(N+2) :
    T,P = work[i]
    DP[i] = max(DP[i-1], DP[i])
    if i + T <= N+1 :
        DP[i+T] = max(DP[i+T], DP[i] + P)

    result = max(result, DP[i])

print(result)
