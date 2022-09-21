from collections import deque, defaultdict

def solution(info, edges):
    global edge_list, result
    
    edge_list = defaultdict(list)
    result = 1
    for start, end in edges :
        edge_list[start].append(end)
    
    p_list = edge_list[0]
    dfs(info, 1, 0, 0, [])
    
    return result

def dfs(info, sheep, wolf, node, p_list) :
    global edge_list, result
    
    # 1. 방문 가능한 노드 추가
    for edge in edge_list[node] :
        p_list.append(edge)
    
    # 2. 양 노드 먼저 방문
    flag = True
    while flag :
        flag = False
        for p in p_list :
            if info[p] == 0 :
                flag = True
                sheep += 1
                result = max(sheep, result)
                for edge in edge_list[p] :
                    p_list.append(edge)
                # 양 노드 방문했으면 리스트에서 삭제
                p_list.remove(p)
    
    # 3. dfs로 늑대 노드 차례대로 방문
    if sheep > (wolf + 1) :
        for p in p_list :
            temp = p_list[:]
            temp.remove(p)
            dfs(info, sheep, wolf+1, p, temp)
    
    