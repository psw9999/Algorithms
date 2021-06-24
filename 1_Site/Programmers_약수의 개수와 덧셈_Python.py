def solution(left, right):
    result = 0
    for i in range (left,right+1) :
        #temp = int(pow(i,1/2))
        temp = int(i**(1/2))
        temp*=temp
        if(i != temp):
            result+=i
        else :
            result-=i
            
    return result
