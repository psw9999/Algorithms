def find_parent(parent, x) :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    
    return parent[x]

def union_parent(parent,a,b) :
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a > b :
        parent[a] = b
    else :
        parent[b] = a
    
def solution(n, costs):
    costs.sort(key = lambda x : x[2])    
    
    result = 0
    parent = []
    for i in range(n) :
        parent.append(i)

    for a,b,cost in costs :
        if find_parent(parent,a) != find_parent(parent,b) :
            result += cost
            union_parent(parent,a,b)
    
    return result