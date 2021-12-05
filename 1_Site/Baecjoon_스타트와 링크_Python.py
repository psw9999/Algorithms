
from itertools import combinations

N = int(input())

graph = []

for _ in range(N) :
    graph.append(list(map(int, input().split())))

comb = list(combinations([i for i in range(0, N)], N//2))

length = len(comb) - 1

result = 200
for i in range(len(comb)//2) :
    temp1 = comb[i]

    temp2 = comb[length - i]
    t1 = 0
    t2 = 0
    for j in range(len(temp1)-1) :
        for z in range(j+1, len(temp1)) : 
            t1 += graph[temp1[j]][temp1[z]] + graph[temp1[z]][temp1[j]]
            t2 += graph[temp2[j]][temp2[z]] + graph[temp2[z]][temp2[j]]
    result = min(result, abs(t1-t2))

print(result)