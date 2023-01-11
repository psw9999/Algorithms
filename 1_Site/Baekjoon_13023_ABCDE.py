import sys
input = sys.stdin.readline

N,M = map(int, input().rstrip().split())
people = [[] for _ in range(N)]

for _ in range(M) :
    a,b = map(int, input().rstrip().split())
    people[a].append(b)
    people[b].append(a)

def dfs(loc, visited, count) :

    if count >= 5 :
        return True
    
    for i in people[loc] :
        if not visited[i] :
            visited[i] = True
            result = dfs(i, visited, count+1)
            if result :
                return result
            visited[i] = False
            
    visited[loc] = False
    return False

visited = [False] * N
for i in range(N) :
    visited[i] = True
    result = dfs(i, visited, 1)
    if result :
        print(1)
        exit(0)
    visited[i] = False

print(0)