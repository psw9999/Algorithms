
n = int(input())
k = list(map(int,input().split()))

DT = [0] * 100

DT[0] = k[0]
DT[1] = max(k[0], k[1])
for i in range(2, n) :
    DT[i] = max(DT[i-1], k[i] + DT[i-2])

print(DT[n-1])