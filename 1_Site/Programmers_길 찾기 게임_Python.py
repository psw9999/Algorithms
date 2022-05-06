from collections import deque,defaultdict
import sys
sys.setrecursionlimit(10000)

def dfs(node, childDict) :
    global result
    result[0].append(node)
    for child in childDict[node] :
        dfs(child, childDict)
    result[1].append(node)

def solution(nodeinfo):
    global result
    temp = []
    for i,node in enumerate(nodeinfo) :
        x,y = node
        temp.append((i+1,x,y))
    temp.sort(key = lambda x : (-x[2],x[1]))
    nodeinfo = deque(temp)
    parent = [[]]
    parent[0].append(nodeinfo.popleft())
    befY = parent[0][0][2]
    nodeHeight = 0
    
    childDict = defaultdict(list)
    rangeDict = defaultdict(list)
    rangeDict[parent[0][0][0]] = [-1,100001]
    
    while nodeinfo :
        node, x, y = nodeinfo.popleft()   
        if befY > y :
            befY = y
            parent.append([])
            nodeHeight += 1
        
        parent[nodeHeight].append((node, x, y))
        for pnode,px,py in parent[nodeHeight-1] :
            minV,maxV = rangeDict[pnode]
            if x > minV and px > x :
                childDict[pnode].append(node)
                rangeDict[node] = [minV, px] 
                break
            if x > px and maxV > x :
                childDict[pnode].append(node)
                rangeDict[node] = [px, maxV]
                break

    result = [[],[]]
    dfs(parent[0][0][0], childDict)
    return result