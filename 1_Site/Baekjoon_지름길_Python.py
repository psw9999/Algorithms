N,D = map(int,input().split())

road = [[] for _ in range(D+1)]
distance = [D] * (D+1)
distance[0] = 0


for _ in range(N) :
    s,e,l = map(int, input().split())
    if e > D or (e-s) <= l :
        continue
    road[s].append((e,l))

for s in range(D) :
    distance[s+1] = min(distance[s]+1, distance[s+1])
    for e,l in road[s] :
        distance[e] = min(distance[e], distance[s] + l)

print(distance[D])
         