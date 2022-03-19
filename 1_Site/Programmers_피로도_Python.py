def dfs(fatigue, dungeons, visited,N) :
    global result
    
    if fatigue <= 0 :
        result = max(result, N)
        return
    
    for i in range(len(dungeons)) :
        if visited[i] == True or dungeons[i][0] > fatigue :
            continue
        else :
            visited[i] = True
            dfs(fatigue - dungeons[i][1], dungeons, visited, N+1)
            visited[i] = False
        
    result = max(result, N)
            
def solution(k, dungeons):
    global result
    result = 0
    visited = [False] * len(dungeons)
    dfs(k,dungeons,visited,0)
    
    return result