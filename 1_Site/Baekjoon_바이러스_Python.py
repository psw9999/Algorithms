
import sys

input = sys.stdin.readline

N = int(input())
computer = [[] for _ in range(N+1)]
visited = [False] * (N+1) 
K = int(input())

for _ in range(K) :
    start, end = map(int, input().rstrip().split())
    computer[start].append(end)
    computer[end].append(start)

queue = [1]
visited[1] = True
while queue :
    cur = queue.pop()
    for c in computer[cur] :
        if visited[c] == True :
            continue
        queue.append(c)
        if (c == 4) :
            print(cur)
        visited[c] = True

print(visited)
print((visited.count(True)-1))
