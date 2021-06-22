def solution(d, budget):
    d.sort()
    cnt,temp = 0,0
    for i in d :
        cnt+=1
        temp+=i
        if temp > budget :
            cnt-=1
            break
    return cnt
