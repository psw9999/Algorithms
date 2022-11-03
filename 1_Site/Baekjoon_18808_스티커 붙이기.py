import sys

input = sys.stdin.readline
global result
N,M,K = map(int, input().rstrip().split())

# 종이 돌리기
def rotatePaper(paper) :
    temp_paper = [[0 for _ in range(len(paper))] for _ in range(len(paper[0]))]
    
    for i in range(len(paper)) :
        for j in range(len(paper[i])) :
            if paper[i][j] == 1 :
                temp_paper[j][-1-i] = 1
            
    return temp_paper

# 노트북 종이 구간 탐색
def checkGraph(graph, paper, startX, startY) :
    global result
    
    if startX + len(paper[0]) > len(graph[0]) :
        return -1
    
    if startY + len(paper) > len(graph):
        return -2
    
    for i in range(len(paper)) :
        for j in range(len(paper[0])) :
            if graph[startY+i][startX+j] and paper[i][j] :
                return 0
    
    # 모두 이상없으면
    for i in range(len(paper)) :
        for j in range(len(paper[0])) :
            if paper[i][j] :
                result += 1
                graph[startY+i][startX+j] += 1
    return 1
    
# 1. 노트북 가로 세로 길이 나타내기
graph = [[0 for _ in range(M)] for _ in range(N)]
papers = []
result = 0

# 2. K개 만큼 종이 갯수 받기
for _ in range(K) :
    R,C = map(int, input().rstrip().split())
    paper = []
    # 2-1. 각 행만큼 종이 맵 입력 받기
    for _ in range(R) :
        paper.append(list(map(int, input().rstrip().split())))
    papers.append(paper)

# 3. 순차적으로 스티커 붙이기
for paper in papers :
    isCompleted = False
    for cnt in range(4) :
        if cnt != 0 :
            paper = rotatePaper(paper)
        
        for startY in range(len(graph)) :
            isYCompleted = False
            for startX in range(len(graph[0])) :
                isXCompleted = False
                temp = checkGraph(graph, paper, startX, startY)

                if temp == 1:
                    isCompleted = True
                    break
                
                if temp == -1 :
                    break
                
                if temp == -2 :
                    isYCompleted = True
            
            if isCompleted or isYCompleted :
                break
        
        if isCompleted :
            break
print(result)
            
            
                     
        
    
            
    


    
    