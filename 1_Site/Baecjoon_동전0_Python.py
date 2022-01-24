
import sys

input = sys.stdin.readline

N,K = map(int, input().rstrip().split())

coin = []

for _ in range(N) :
    coin.append(int(input()))

maxIndex = len(coin)-1
result = 0

while K > 0 :
    for i in range(maxIndex, -1, -1) :
        if coin[i] <= K :
            maxIndex = i
            break
    result += (K // coin[maxIndex])
    K =  K % coin[maxIndex]
    print(K)

print(result)    