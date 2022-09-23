
import sys

input = sys.stdin.readline

N = int(input().rstrip())
numbers = []
for _ in range(N) :
    numbers.append(int(input().rstrip()))

DP = [1 for _ in range(N)]

for i in range(N) :
    for j in range(i) :
        if numbers[i] > numbers[j] :
            DP[i] = max(DP[i], DP[j] + 1)

print(N - max(DP))