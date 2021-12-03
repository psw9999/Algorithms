
N = int(input())

health = list(map(int,input().split()))
value = list(map(int,input().split()))
K = [[0] * 100 for _ in range(N+1)]

for i in range(len(K)) :
    for h in range(len(K[i])) :
        if i == 0 or h == 0 :
            continue
        if health[i-1] > h :
            K[i][h] = K[i-1][h]
        else :
            K[i][h] = max(value[i-1] + K[i-1][h-health[i-1]], K[i-1][h])

print(K[N][99])