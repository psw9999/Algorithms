n,k = map(int, input().split())

arr = []
dp = [0] * 10001

for i in range(n) :
    temp = int(input())
    if temp <= 10000 :
        arr.append(temp)
        
dp[0] = 1
arr.sort()

for i in arr:
    for j in range(1, k + 1):
        if j - i >= 0:
            dp[j] += dp[j - i]

for i in range(11) :
    print(dp[i], end=' ')
