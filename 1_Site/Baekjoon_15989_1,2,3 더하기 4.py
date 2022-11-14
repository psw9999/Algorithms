import sys

input = sys.stdin.readline
T = int(input().rstrip())
testCases = []
for _ in range(T) :
    testCases.append(int(input().rstrip()))

dp = [1] * 10001
for i in range(2, 10001) :
    dp[i] += dp[i-2]

for i in range(3, 10001) :
    dp[i] += dp[i-3]

for testCase in testCases :
    print(dp[testCase])