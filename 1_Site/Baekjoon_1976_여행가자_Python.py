import sys

input = sys.stdin.readline

def find_parent(parent, x) :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b :
        parent[b] = a
    else :
        parent[a] = b

# 도시의 수 : N
N = int(input().rstrip())
# 여행 계획에 속한 도시들의 수 : M
M = int(input().rstrip())

parent = [0] * (N)
for i in range(N) :
    parent[i] = i

for i in range(N) :
    temp = list(map(int, input().rstrip().split()))
    for j in range(N) :
        if temp[j] == 1 :
            union_parent(parent,i,j)
            
# 여행계획 (원소에 -1 해주기)
plan = list(map(int, input().rstrip().split()))
flag = True
for i in range(M-1) :
    if parent[plan[i]-1] != parent[plan[i+1]-1] :
        flag = False
        break

if flag : 
    print('YES')
else :
    print('NO')


