import sys

input = sys.stdin.readline

N,M = map(int, input().rstrip().split())

# 0 : 작다, 1 : 크다
dp = [[[] for _ in range(2)] for _ in range(N+1)]
result = [[set() for _ in range(2)] for _ in range(N+1)]

for _ in range(M) :
    first, second = map(int, input().rstrip().split())
    dp[first][0].append(second)
    dp[second][1].append(first)

def dfs(number, check) :

    if len(result[number][check]) != 0 :
        return
    
    else :
        result[number][check].add(number)
        
        for n in dp[number][check] :
            dfs(n, check)
            
            for i in result[n][check] :
                result[number][check].add(i)

for i in range(2) :
    for j in range(1, N+1) :
        dfs(j, i)

answer = 0
for i in range(1, N+1) :
    if N == (len(result[i][0]) + len(result[i][1]) - 1) :
        answer += 1

print(answer) 
            
            