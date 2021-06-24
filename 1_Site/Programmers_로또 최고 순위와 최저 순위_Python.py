def solution(lottos, win_nums):
    grade = [6,6,5,4,3,2,1]
    zero = 0
    min_cnt = 0
    
    # 내가 짠 방식
    # for i in lottos :
    #     if i == 0 :
    #         zero+=1
    #         continue
    #     for j in win_nums :
    #         if i == j :
    #             min_cnt+=1
    
    zero = lottos.count(0)
    for i in win_nums:
        if i in lottos :
            min_cnt+=1
    
    return [grade[min_cnt+zero], grade[min_cnt]]
