
import sys

# 루트 노트가 아니라면, 루트 노드를 찾을때까지 재귀적으로 호출
def find_parent(parent, i) :
    if i != parent[i] :
        parent[i] = find_parent(parent, parent[i])
    return parent[i]

def union_parent(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a > b :
        parent[a] = b
    else :
        parent[b] = a
     

input = sys.stdin.readline
INF = int(1e9)
N,M = map(int, input().rstrip().split())

parent = [i for i in range(N+1)]
edges = []
for _ in range(M) :
    a,b,c = map(int, input().rstrip().split())
    edges.append((c,a,b))

edges.sort(key = lambda x: x[0])
result = 0
maxV = 0
for cost, a, b in edges :
    if find_parent(parent, a) != find_parent(parent, b) :
        union_parent(parent, a, b)
        maxV = max(maxV, cost)
        result += cost

print(result - maxV)