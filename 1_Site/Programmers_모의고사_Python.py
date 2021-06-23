def solution(answers):
    num = len(answers)
    list_1 = [1,2,3,4,5]
    l1_ord = len(list_1)
    
    list_2 = [2,1,2,3,2,4,2,5]
    l2_ord = len(list_2)
        
    list_3 = [3,3,1,1,2,2,4,4,5,5]
    l3_ord = len(list_3)    
    
    score = [0,0,0]
    for i in range(num) :
        if answers[i] == list_1[i%l1_ord] :
            score[0]+=1
        if answers[i] == list_2[i%l2_ord] :
            score[1]+=1
        if answers[i] == list_3[i%l3_ord] :
            score[2]+=1
    result = []
    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
"""
# 내가 한 방식
    mmax = max(score_1, score_2, score_3)
    result = []
    if(mmax == score_1) :
        result.append(1)
    if(mmax == score_2) :
        result.append(2)
    if(mmax == score_3) :
        result.append(3)
"""
