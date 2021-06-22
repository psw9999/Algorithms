def solution(n,lost, reserve) :
    result = [1 for i in range(n)]
    for i in lost :
        result[i-1] -=1
    
    n-=len(lost)
    
    for i in reserve :
        result[i-1] +=1
        if(result[i-1] == 1) : 
            n+=1
        
    for i in range(len(result)-1) :
        temp = result[i] - result[i+1]
        if(temp == -2) :
            result[i+1] = 1
            n+=1
            
        elif(temp == 2) :
            result[i+1] = 1
            n+=1    

    return n
