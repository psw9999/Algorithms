
N,K = map(int, input().split())

coin = []
maxV = K+1
DP = [maxV] * (maxV)
DP[0] = 0
for _ in range(N) :
    coin.append(int(input()))

for i in range(K) :
    for c in coin :
        if i+c <= K :
            DP[i+c] = min(DP[i+c], DP[i]+1)

if DP[K] == maxV :
    print(-1)
else :
    print(DP[K])