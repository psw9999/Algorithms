
N, K = map(int, input().split())

val, wei = [], []

# 물품 갯수만큼 행의 수 생성, 무게 한도만큼 열의 수 생성
P = [[0] * (K+1) for _ in range(N+1)]

for _ in range(N) :
    t1,t2 = map(int, input().split())
    wei.append(t1)
    val.append(t2)

for i in range(len(P)) :
    for w in range(len(P[i])) :
        # 물품이 0개거나, 무게 한도가 0인 경우는 계산 X
        if i == 0 or w == 0 :
            continue
        # i번째 보석이 무게 한도보다 무거운 경우 
        if wei[i-1] > w :
            # i-1번째 보석의 가치를 가져옴. 
            P[i][w] = P[i-1][w]
        else :
            P[i][w] = max(val[i-1] + P[i-1][w-wei[i-1]], P[i-1][w])

print(P)
print(P[N][K])
            
        
    
