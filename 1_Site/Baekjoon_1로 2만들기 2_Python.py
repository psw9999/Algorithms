
N = int(input())

DP = [0] * (N+1)

DP[1] = (1,0)

calcul = (2,3)

for i in range(1,N) :
    if DP[i+1] == 0 or DP[i][1] < DP[i+1][1]:
        DP[i+1] = (1,DP[i][1]+1)
    for c in calcul :
        if i*c > N :
            continue
        if DP[i*c] == 0 or DP[i][1] < DP[i*c][1] :
            DP[i*c] = (c,DP[i][1]+1)

print(DP[N][1])

while N > 0 :
    print(N,end = ' ')
    if DP[N][0] == 1 :
        N -= 1
    else :
        N //= DP[N][0]
    
    