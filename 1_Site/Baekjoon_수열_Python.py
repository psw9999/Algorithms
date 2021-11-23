n,k = map(int, input().split())

arr = []
dp = [0] * 10001

for i in range(n) :
    temp = int(input())
    if temp <= 10000 :
        arr.append(temp)

arr.sort()

for i in range(k+1) :
    if dp[i] >= 1 :
        for j in range(n) :
            dp[i+arr[j]] += dp[i] + 1

for i in range(11) :
    print(dp[i], end=' ')
