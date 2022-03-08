def solution(n, results):
    arrs = []
    answer = 0
    for i in range(0,n+1) :
        arrs.append([])
        arrs[i].append([])
        arrs[i].append([])

    for win,lose in results :
        arrs[win][0].append(lose)
        arrs[lose][1].append(win)
    
    
    for wins,loses in arrs :
        for win in wins :
            temps = arrs[win][0]
            for temp in temps :
                if not temp in wins :
                    wins.append(temp)
        
        for lose in loses :
            temps = arrs[lose][1]
            for temp in temps :
                if not temp in loses :
                    loses.append(temp)
        
        if len(wins) + len(loses) >= (n-1) :
            answer += 1
         
    return answer