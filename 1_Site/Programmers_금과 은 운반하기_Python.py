def dfs(user_id, cnt, visited, temp) :
    global result
    global ban_list
    
    if cnt == len(ban_list) :
        temp.sort()
        if temp not in result :
            result.append(temp)
        return
    
    for i, user in enumerate(user_id) :
        if visited[i] :
            continue
        # 문자열의 길이가 다르다면 continue
        if len(user) != ban_list[cnt][0] :
            continue
        flag = True
        for z in range(1,len(ban_list[cnt])) :
            loc, s = ban_list[cnt][z]
            if user[loc] != s :
                flag = False
                break
            
        if flag :
            visited[i] = True
            dfs(user_id, cnt+1, visited, temp + [i])
            visited[i] = False
    
def solution(user_id, banned_id):
    global result
    global ban_list
    
    ban_list = []
    for i,ban in enumerate(banned_id) :
        ban_list.append([])
        ban_list[i].append(len(ban))
        for j,s in enumerate(ban) :
            if s == '*' :
                continue
            else :
                ban_list[i].append((j,s))

    visited = [False] * len(user_id)
    result = []
    
    dfs(user_id, 0, visited, [])
    return len(result)