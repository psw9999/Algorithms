
import sys
import heapq

input = sys.stdin.readline

N = int(input())
queue = []
for _ in range(N) :
    count = int(input())
    heapq.heappush(queue, count)
    
result = 0

for _ in range(N-1) :
    temp = 0
    temp += heapq.heappop(queue)
    temp += heapq.heappop(queue)
    result += temp
    heapq.heappush(queue, temp)

print(result)