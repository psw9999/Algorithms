def solution(people, limit):
    people.sort()
    people_num = len(people)
    result = 0
    cur = 0
    for i in range(len(people)-1,0,-1) :
        #가운데 원소로 겹치는 경우 break
        if cur == i :
            return result + 1
        
        temp = people[cur] + people[i]
        if temp <= limit :
            people_num-=2
            cur+=1
        else :
            people_num-=1
        result += 1
        
        if(people_num == 0) :
            return result
    return result + 1