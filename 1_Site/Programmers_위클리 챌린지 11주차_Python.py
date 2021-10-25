def solution(k, dungeons):
    result = 0
    temp = []

    dungeons.sort(key = lambda x : (-(x[0]-x[1]),x[1]))
    print(dungeons)
    
    while dungeons and k > 0: 
        if k < dungeons[0][0] :
            del dungeons[0]
            
        else :
            result += 1
            k = k - dungeons[0][1]
            del dungeons[0]
        
    return result