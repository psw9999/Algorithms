import sys
import heapq

input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T) :
    
    K = int(input().rstrip())
    queue = list(map(int, input().rstrip().split()))
    heapq.heapify(queue)
    result = 0
    while len(queue) >= 2 :
        first, second = heapq.heappop(queue), heapq.heappop(queue)
        result += (first + second)
        heapq.heappush(queue, (first + second))
    
    print(result)