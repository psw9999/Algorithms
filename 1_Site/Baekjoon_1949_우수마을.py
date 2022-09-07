
import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline

N = int(input())
population = list(map(int, input().rstrip().split()))
relations = [[] for _ in range(N)]
DP = [[0,0] for _ in range(N)]
visited = [False] * N

for _ in range(N-1) :
    i, j = map(int, input().rstrip().split())
    relations[i-1].append(j-1)
    relations[j-1].append(i-1)
    
def dfs(index) :
    global visited, DP, relations, population
    
    visited[index] = True
    DP[index][1] += population[index]
    
    for number in relations[index] :
        if not visited[number] :
            dfs(number)
            DP[index][0] += max(DP[number][1],DP[number][0])
            DP[index][1] += DP[number][0]
            
dfs(0)
print(max(DP[0][0], DP[0][1]))