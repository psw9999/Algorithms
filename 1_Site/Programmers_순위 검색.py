from collections import defaultdict

def solution(info, query):
    global user_info
    user_info = defaultdict(list)
    for user in info :
        temp_list = user.split(" ")
        dfs("", 0, temp_list)
    
    for key in user_info.keys() :
        user_info[key].sort()
    
    result = []
    for q in query :
        q = q.replace(" and ","").split(" ")
        score_list = user_info[q[0]]
        if len(score_list) == 0 :
            result.append(0)
        else :
            #score_list.sort()
            loc = search(score_list, int(q[1]))
            result.append(len(score_list) - loc)
    
    return result
        
        
def dfs(string, depth, temp_list) :
    global user_info
    
    if depth == 4 :
        user_info[string].append(int(temp_list[depth]))
    
    else :
        dfs(string + "-", depth + 1, temp_list)
        dfs(string + temp_list[depth], depth + 1, temp_list)


def search(score_list, target) :
    left, right = 0, len(score_list)
    
    while left < right :
        mid = (left + right) // 2
        
        if score_list[mid] >= target :
            right = mid
        
        else :
            left = mid + 1
            
    return left
    
    