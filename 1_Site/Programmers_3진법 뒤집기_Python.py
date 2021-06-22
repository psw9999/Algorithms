def solution(n):
    i,j = 1,1
    result = 0
    while(i <= n):
        i*=3
    i/=3
    while(n > 0):
        if(n >= 2*i) :
            n -= 2*i
            result += 2*j
        elif(n >= i) :
            n -= i
            result += j
        
        i /= 3
        j *= 3

    return result
