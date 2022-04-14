def solution(stones, k):
    left, right = 0,200000000
    result = 0
    
    while left <= right :
        # 건너간 횟수 : mid
        mid = ((left + right) // 2)
        cnt = 0
        
        for stone in stones :
            if stone < mid :
                cnt += 1
            else :
                cnt = 0
            
            if cnt >= k :
                break
        
        if cnt >= k :
            right = mid - 1
        
        else :
            left = mid + 1
            result = max(result, mid)
    
    return result
            