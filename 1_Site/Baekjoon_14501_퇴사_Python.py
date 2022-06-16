import sys

input = sys.stdin.readline

N = int(input())
DP = [0] * (N+1)
work = []
for _ in range(N) :
    T,P = map(int, input().rstrip().split())
    work.append((T,P))

result = 0
for i in range(N-1, -1, -1) :
    T,P = work[i]
    if i+T <= N :
        result = max(result, DP[i+T]+P)
    DP[i] = result

print(result)
