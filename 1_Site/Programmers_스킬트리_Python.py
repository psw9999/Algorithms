# 1. 파이썬은 문자열을 인덱스 형식으로 접근이 가능하다. (temp = "ABCD", temp[0] = "A")
# 2. 문자열의 길이가 다를 때 다른 사람의 소스처럼 길이를 지정해서 특정 길이까지만 비교가 가능하다.

# 내 소스
def solution(skill, skill_trees):
    result = 0
    for st in skill_trees :
        idx = 0
        idx_max = len(skill)
        flag = False
        
        for ap in st :
            if ap == skill[idx] :
                if idx < idx_max-1 :
                    idx+=1
                else :
                    break
                    
            else :
                for i in range(idx+1, len(skill)) :
                     if ap == skill[i] :
                            flag = True
                            break
                if flag == True :
                    break
                    
        if flag == False :
            result+=1
    
    return result

# 다른 사람의 소스
def solution(skill,skill_tree):
    answer=0
    for i in skill_tree:
        skillist=''
        for z in i:
            if z in skill:
                skillist+=z
        #핵심
        if skillist==skill[0:len(skillist)]:
            answer+=1
    return answer