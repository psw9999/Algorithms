import sys

input = sys.stdin.readline
N,M = map(int, input().rstrip().split())
lengths = list(map(int, input().rstrip().split()))

left, right = 0, sum(lengths)
result = right

while left <= right :
    mid = (left + right) // 2
    count = 1
    flag = True
    count_sum = 0
    
    for length in lengths :
        count_sum += length
        
        if length > mid :
            flag = False
            break
        
        if count_sum > mid :
            count += 1
            count_sum = length
            
            if count > M :
                flag = False
                break
    
    if not flag :
        left = mid + 1
    
    else :
        result = min(mid, result)
        right = mid - 1

print(result)
