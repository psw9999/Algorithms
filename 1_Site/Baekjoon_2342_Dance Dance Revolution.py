import sys

input = sys.stdin.readline
movements = list(map(int, input().rstrip().split()))
length = len(movements)
MAX = int(1e9)
dp = [[[MAX for _ in range(5)] for _ in range(5)] for _ in range(length)]
dp[0][0][0] = 0

def move(cur, target) :
    if cur == 0 :
        return 2
    
    elif cur == target :
        return 1
    
    elif abs(cur-target) == 2 :
        return 4
    
    else :
        return 3

for (i, m) in enumerate(movements) :
    
    if m == 0 :
        break

    for left in range(5) :
        for right in range(5) :
            if dp[i][left][right] == MAX :
                continue
            dp[i+1][left][m] = min(dp[i+1][left][m], dp[i][left][right] + move(right, m))
            dp[i+1][m][right] = min(dp[i+1][m][right], dp[i][left][right] + move(left, m))

result = MAX
for i in range(5) :
    for j in range(5) :
        result = min(dp[length-1][i][j], result)

print(result)    
    
