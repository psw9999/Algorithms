import sys
input = sys.stdin.readline
from itertools import combinations

N = int(input().rstrip())
mp,mf,ms,mv = map(int, input().rstrip().split())
foods = []
for _ in range(N) :
    p,f,s,v,c = map(int, input().rstrip().split())
    foods.append((p,f,s,v,c))
indexes = [i for i in range(1,N+1)]

result = int(1e9)
resultIndex = []

for i in range(1, N+1) :
    for comb in combinations(indexes, i) :
        n = [0,0,0,0]
        amount = 0
        for j in comb :
            p,f,s,v,c = foods[j-1]
            
            amount += c
            n[0] += p
            n[1] += f
            n[2] += s
            n[3] += v

            # 필수 영양소를 모두 충족하는가?
            if n[0] >= mp and n[1] >= mf and n[2] >= ms and n[3] >= mv and result >= amount :
                if amount == result :
                    resultIndex.append(comb)
                else :
                    result = amount
                    resultIndex = [comb]
                break

if result != int(1e9) :
    print(result)
    resultIndex.sort()
    print(' '.join(list(map(str, resultIndex[0]))))

else :
    print(-1)

