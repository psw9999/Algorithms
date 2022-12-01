import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int, input().rstrip().split())
orders = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

# 앞 사람의 번호 담기
for _ in range(M) :
    A,B = map(int, input().rstrip().split())
    orders[A].append(B)
    indegree[B] += 1
 
# queue에 앞 사람이 몇인지 담기
def topology_sort() :
    result = []
    queue = deque()
    
    for i in range(1, N+1) :
        if indegree[i] == 0 :
            queue.append(i)
    
    while queue :
        now = queue.popleft()
        result.append(now)
        
        for i in orders[now] :
            indegree[i] -= 1
            
            if indegree[i] == 0 :
                queue.append(i)
    
    print(' '.join(list(map(str,result))))
    
topology_sort()
