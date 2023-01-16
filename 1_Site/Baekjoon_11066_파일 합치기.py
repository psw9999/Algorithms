import sys
input = sys.stdin.readline

MAX = int(1e9)
T = int(input())

for _ in range(T) :
    K = int(input())
    pages = list(map(int, input().rstrip().split()))
    totals = [0] * (K + 1)
    for (i,page) in enumerate(totals) :
        if i == 0 :
            continue
        totals[i] = totals[i-1] + pages[i-1]
        
    dp = [[MAX for _ in range(K)] for _ in range(K)]
    
    for i in range(K) :
        dp[i][i] = 0
    
    for d in range(1, K) :
        for start in range(K-d) :
            end = start + d
            
            for k in range(start, end) :
                dp[start][end] = min(dp[start][end], dp[start][k] + dp[k+1][end] + (totals[end+1] - totals[start]))
    print(dp[0][-1])
