from collections import defaultdict

def solution(id_list, report, k):
    id_dict = defaultdict(list)
    users = defaultdict(int)
    result = defaultdict(int)
    
    for ID in id_list :
        id_dict[ID] = []
        result[ID] = 0
        
    report = list(set(report))
    
    while report :
        user1, user2 = map(str, report.pop().split())
        id_dict[user1].append(user2)
        users[user2]+=1
    
    for user in users :
        if users[user] >= k :
            for ID in id_dict :
                if user in id_dict[ID] :
                    result[ID] += 1
    
    return list(result.values())