import sys

input = sys.stdin.readline
N = int(input().rstrip())

rods = []
result = 0
for _ in range(N) :
    L,H = map(int, input().rstrip().split())
    rods.append((L,H))

rods.sort(key = lambda x:x[1])
l,h = rods.pop()
minV, maxV = l,l
result += h

while rods :
    l,h = rods.pop()
    if l < minV :
        result += (minV - l) * h
        minV = l
    
    if l > maxV :
        result += (l - maxV) * h
        maxV = l

print(result)