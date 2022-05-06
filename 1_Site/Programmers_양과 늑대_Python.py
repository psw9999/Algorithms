# from collections import defaultdict
# import heapq
# import math

# def findSheep(info, cur) :
#     global wolfDict, childDict
#     temp = 0
#     for child in childDict[cur] :
#         temp += findSheep(info,child)
    
#     if info[cur] == 1 :
#         wolfDict[cur] = temp
    
#     if info[cur] == 0 :
#         return temp + 1
#     else :
#         return temp

# # dfs로 늑대 밑에 몇마리의 양이있는지 체크
# def dfs(info, cur, cnt) :
#     global queue, wolfDict, childDict
    
#     # 양이라면 힙큐에 넣기
#     if info[cur] == 0 :
#         heapq.heappush(queue,cnt)
    
#     # 늑대라면 가중치 계산
#     else :
#         if wolfDict[cur] == 0 :
#             return
#         cnt += 1 / wolfDict[cur]
#     for child in childDict[cur] :
#         dfs(info, child, cnt)
    
# def solution(info, edges):
#     global queue,childDict,wolfDict
#     queue = []
#     wolfDict = defaultdict(int)
#     childDict = defaultdict(list)  
#     for p,c in edges :
#         childDict[p].append(c)
#     findSheep(info, 0)
#     dfs(info, 0, 0)
#     result = 1
#     heapq.heappop(queue)
#     cnt = 0
    
#     while queue :
#         cnt += heapq.heappop(queue)
#         if cnt % 1 != 0 :
#             temp = math.ceil(cnt)
#         else :
#             temp = cnt
#         if temp >= result :
#             return result
#         result += 1
    
#     return result

from collections import defaultdict

def solution(info, edges):
    global result,parentDict
    result = 0
    parentDict = defaultdict(list)
    
    for p,c in edges :
        parentDict[p].append(c)

    dfs(info, 1,0, parentDict[0][:])
    return result
    
def dfs(info, sheep, wolf, nodes) :
    global result,parentDict
    result = max(result, sheep)
    for node in nodes :
        # 노드가 늑대인 경우
        if info[node] == 1 :
            # 늑대+1이 양보다 크거나 같으면 dfs 수행 안함
            if sheep <= wolf + 1 :
                continue
            temp = nodes[:]
            temp.remove(node)
            dfs(info, sheep, wolf+1, temp + parentDict[node])
        
        # 노드가 양인 경우
        else :
            temp = nodes[:]
            temp.remove(node)
            dfs(info, sheep+1, wolf, temp + parentDict[node])
        