def solution(brown, yellow):
    x = 1
    y = 1
    while True :
        if yellow % y == 0 :
            x = yellow / y
            total = 4 + (x * 2) +  (y * 2)
        if brown == total :
            break
        y+=1
        
    return [max(x,y)+2, min(x,y)+2]