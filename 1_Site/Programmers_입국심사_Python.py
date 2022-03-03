def solution(n, times):
    left, right = 1, max(times) * n
    mid = (right + left) // 2
    result = 0
    while right >= left :
        temp = 0
        for time in times :
            temp += mid // time
            if temp >= n :
                break
        
        if temp >= n :
            result = mid
            right = mid - 1
        else :
            left = mid + 1
        mid = (right + left) // 2
    
    return result