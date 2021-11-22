import sys

n,m = map(int, sys.stdin.readline().split())
array = list(map(int,sys.stdin.readline().split()))

dv = 0

for i in range(m) :
    dv += array[i]  
max_value = dv

tp = 0
for i in range(m, n) :
    dv = dv-array[tp]+array[i]
    tp += 1
    max_value = max(max_value,dv)
       
print(max_value)
