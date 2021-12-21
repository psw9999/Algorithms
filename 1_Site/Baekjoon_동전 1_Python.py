n,k = map(int, input().split())

arr = []
dp = [0] * 10001

for _ in range(n) :
    arr.append(int(input()))
        
dp[0] = 1
arr.sort()

for i in arr:
    for j in range(1, k + 1):
        if j - i >= 0:
            dp[j] += dp[j - i]
    for i in range(1, 11) :
        print(dp[i], end=' ')
    
# for i in range(1, 11) :
#     print(dp[i], end=' ')
