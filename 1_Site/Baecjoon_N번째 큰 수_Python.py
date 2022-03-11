import sys
from heapq import heappop, heappush,heapify

input = sys.stdin.readline

N = int(input())
second = int(-1e9)

queue = []
queue = list(map(int, input().rstrip().split()))
heapify(queue)

for _ in range(1, N) :
    temp = list(map(int, input().rstrip().split()))
    
    for t in temp :
        if t > queue[0] :
            heappush(queue,t)
            heappop(queue)

print(queue[0])