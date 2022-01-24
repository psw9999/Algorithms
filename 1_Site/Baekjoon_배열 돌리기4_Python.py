
from itertools import permutations
import sys

input = sys.stdin.readline
result = int(1e9)

def dfs(v) :
    #print(str(v)+"번째")
    global visited, result
    visited[v] = True
    r,c,s = iter[v][0],iter[v][1],iter[v][2]
    rotate(c-s-1,r-s-1,c+s-1,r+s-1)
    temp_list = []
    
    for i in range(len(visited)) :
        if not visited[i] :
            temp_list.append(i)
            
    if not temp_list :
        sum_arr()
    
    else :
        for t in temp_list :
            dfs(t)
    
    reverse(c-s-1,r-s-1,c+s-1,r+s-1)
    visited[v] = False
    
def rotate(sx,sy,ex,ey) :
    global graph
    if sx >= ex or sy >= ey :
        return
    
    temp = graph[sy][sx]
    for i in range(sx,ex) :
        temp2 = graph[sy][i+1]
        graph[sy][i+1] = temp
        temp = temp2
    
    for i in range(sy,ey) :
        temp2 = graph[i+1][ex]
        graph[i+1][ex] = temp
        temp = temp2
    
    for i in range(ex,sx,-1) :
        temp2 = graph[ey][i-1]
        graph[ey][i-1] = temp
        temp = temp2
    
    for i in range(ey,sy,-1) :
        temp2 = graph[i-1][sx]
        graph[i-1][sx] = temp
        temp = temp2 
    
    rotate(sx+1,sy+1,ex-1,ey-1)
    
def reverse(sx,sy,ex,ey) :
    global graph
    if sx >= ex or sy >= ey :
        return
    
    temp = graph[sy][sx]
    for i in range(sy,ey) :
        temp2 = graph[i+1][sx]
        graph[i+1][sx] = temp
        temp = temp2
        
    for i in range(sx,ex) :
        temp2 = graph[ey][i+1]
        graph[ey][i+1] = temp
        temp = temp2         
        
    for i in range(ey,sy,-1) :
        temp2 = graph[i-1][ex]
        graph[i-1][ex] = temp
        temp = temp2    
        
    for i in range(ex,sx,-1) :
        temp2 = graph[sy][i-1]
        graph[sy][i-1] = temp
        temp = temp2
    
    reverse(sx+1,sy+1,ex-1,ey-1)     

def sum_arr() :
    global result
    minV = 1e9
    for i in range(len(graph)) :
        minV = min(minV,sum(graph[i]))
    result = min(result, minV)
    return

N,M,K = map(int, input().rstrip().split())

graph = []
for _ in range(N) :
    graph.append(list(map(int, input().rstrip().split())))

iter = []
visited = [False] * K
for _ in range(K) :
    r,c,s = map(int,input().rstrip().split())
    iter.append((r,c,s))

for i in range(K) :
    #visited[i] = True
    dfs(i)
    #visited[i] = False

print(result)
    
