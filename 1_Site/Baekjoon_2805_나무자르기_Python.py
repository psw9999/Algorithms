
import sys

input = sys.stdin.readline
N,M= map(int,input().rstrip().split())
trees = list(map(int,input().rstrip().split()))

trees.sort()
left,right = 0,trees[N-1]
result = 0

while right >= left :
    mid = (right + left) // 2
    temp = 0
    for i in range(N) :
        if trees[i] <= mid :
            continue     
        else :
            temp += trees[i] - mid
    
    if temp >= M :
        result = max(result, mid)
        left = mid + 1
    else :
        right = mid-1
    
print(result)



    
    
    