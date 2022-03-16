from collections import defaultdict

def find_parent(parent, result, profit, seller) :
    sell = seller
    prof = profit
    flag = False
    while True :
        temp = prof // 10
        if temp == 0 :
            flag = True
        result[sell] += prof - temp
        if parent[sell] == sell :
            break
        
        else :
            prof = temp
            sell = parent[sell]
        
        if flag :
            break

def solution(enroll, referral, seller, amount):
    parent = defaultdict(str)
    result = defaultdict(int)
    sell = defaultdict(int)
    
    for i in range(len(enroll)) :
        if referral[i] == "-" :
            parent[enroll[i]] = enroll[i]
        else :
            parent[enroll[i]] = referral[i]
        
        result[enroll[i]] = 0
        
    # seller 합치기
    for i in range(len(seller)) :
        sell[seller[i]] += amount[i]
    
    for i in range(len(seller)) :
        find_parent(parent, result, amount[i] * 100, seller[i])
    
    return list(result.values())