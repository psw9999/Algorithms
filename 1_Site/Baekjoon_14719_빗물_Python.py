
import sys

input = sys.stdin.readline
H,W = map(int,input().rstrip().split())
graph = [[0 for _ in range(W)] for _ in range(H)]
temp = list(map(int,input().rstrip().split()))
wall = sum(temp)

for idx,t in enumerate(temp) :
    for i in range(t) :
        graph[H-i-1][idx] = -1

result = 0
for line in graph :
    start = -1
    end = -1
    temp = 0
    for i in range(len(line)) :
        
        # 스타트 벽을 못찾았을 때
        if start == -1 :
            if line[i] == -1 :
                start = i
            else :
                continue
        
        elif end == -1 :
            if line[i] == -1 :
                end = i
                temp += end-start-1
                start = end
                end = -1
            else :
                continue
             
    result += temp

print(result)      
            
            
        
              
                
        





    
    
    