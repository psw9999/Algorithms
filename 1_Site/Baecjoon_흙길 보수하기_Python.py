
import sys

input = sys.stdin.readline

N,L = map(int, input().rstrip().split())

pool = []

for _ in range(N) :
    t1,t2 = map(int, input().rstrip().split())
    pool.append((t1,t2))

pool.sort()
print(pool)
start = 0
result = 0
for p1,p2 in pool :
    
    if p1 > start :
        start = p1
    
    temp = (p2-start) / L
    temp2 = (p2-start) // L
    if temp > temp2 :
        temp2 += 1
    result += temp2
    start = start + (L*temp2)
    print(start)

print(result)
