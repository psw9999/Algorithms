
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
N = int(input().rstrip())
tree = [[] for _ in range(N+1)]
DP = [[0,0] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(N-1) :
    u,v = map(int, input().rstrip().split())
    if u <= v :
        tree[u].append(v)
    else :
        tree[v].append(u)

def visitNode(n) :
    visited[n] = True
    DP[n][0] = 0
    DP[n][1] = 1
    for i in tree[n] :
        # if visited[i] :
        #     continue
        visitNode(i)
        DP[n][0] += DP[i][1]
        DP[n][1] += min(DP[i][0],DP[i][1])

visitNode(1)

print(min(DP[1][0],DP[1][1]))