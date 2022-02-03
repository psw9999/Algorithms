
from collections import deque
import sys

input = sys.stdin.readline

N,d,k,c = map(int, input().rstrip().split())

sushi = deque()
cur = deque()
kinds = {}
kinds[c] = 1
result = 0
for _ in range(N) :
    sushi.append(int(input()))

for _ in range(k) :
    temp = sushi.popleft()
    cur.append(temp)
    if not temp in kinds :
        kinds[temp] = 1
    else :
        kinds[temp] += 1
result = len(kinds)

for _ in range(1,N) :
    temp = cur.popleft()
    sushi.append(temp)
    kinds[temp] -= 1
    if kinds[temp] == 0 :
        kinds.pop(temp)
    
    temp = sushi.popleft()
    cur.append(temp)
    if not temp in kinds :
        kinds[temp] = 1
    else :
        kinds[temp] += 1
    result = max(result, len(kinds))
    

print(result)