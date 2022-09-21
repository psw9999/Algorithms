
import sys

input = sys.stdin.readline

N = int(input().rstrip())
numbers = list(map(int,input().rstrip().split()))
M = int(input().rstrip())
DP = [[0 for _ in range(N+1)] for _ in range(N+1)]
questions = []
for _ in range(M) :
    start, end = map(int, input().rstrip().split())
    questions.append((start, end))

# 문자열 한 개
for i in range(1, N+1) :
    DP[i][i] = 1

# 문자열 두 개
for i in range(1, N) :
    if numbers[i-1] == numbers[i] :
        DP[i][i+1] = 1

# 문자열 세 개 이상
for l in range(2, N) :
    for i in range(1, N-l+1) :
        if numbers[i-1] == numbers[i+l-1] and DP[i+1][i+l-1] == 1 :
            DP[i][i+l] = 1

for start, end in questions :
    print(DP[start][end])


