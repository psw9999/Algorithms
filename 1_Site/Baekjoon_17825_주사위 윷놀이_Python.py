# 내 풀이
import sys
input = sys.stdin.readline

def dfs(horseNum,diceNum,temp,cnt) :
    global graph,dices,horse,result
    ttempHorse = horse[horseNum][:]
    
    # 말이 도착지점에 있는 경우
    if horse[horseNum][0] < 0 :
        return ttempHorse
    
    tempHorse = horse[horseNum][:]
    tempHorse[1] += diceNum

    # 도착지점 이상으로 가는 경우
    # [0,2,4,6,8,-1,12,14,16,18,-2,22,24,26,28,-3,32,34,36,38,-5],
    
    while tempHorse[1] >= (len(graph[tempHorse[0]])-1) :
        if tempHorse[0] == 5 :
            tempHorse[0] = -1 * (horseNum+1)
            tempHorse[1] = -1
            break
                
        tempHorse[1] = tempHorse[1] - (len(graph[tempHorse[0]])-1)
        tempHorse[0] = (graph[tempHorse[0]][-1]) * -1

            
    # 파란 화살표
    #elif tempHorse[0] == 0 and (tempHorse[1] % 5) == 0 and tempHorse[1] != 20 :
    if tempHorse[0] >= 0 and graph[tempHorse[0]][tempHorse[1]] < 0 :
        tempHorse[0] = graph[tempHorse[0]][tempHorse[1]] * -1
        tempHorse[1] = 0
        
    # 이동하는 칸에 다른 말이 존재하는 경우
    for h in horse :
        if h == tempHorse :
            return ttempHorse
    
    if tempHorse[0] >= 0 :
        temp += graph[tempHorse[0]][tempHorse[1]]
    horse[horseNum] = tempHorse
    
    # 재귀 완료시 돌아감
    if cnt == 10 :
        result = max(result, temp)
        return ttempHorse
    
    # dfs 다시 실행
    for i in range(4) :
        tHorse = dfs(i,dices[cnt],temp,cnt+1)
        horse[i] = tHorse
    
    return ttempHorse
        
dices = list(map(int, input().rstrip().split()))

graph = [
    [0,2,4,6,8,-1,12,14,16,18,-2,22,24,26,28,-3,32,34,36,38,-5],
    [10,13,16,19,-4],
    [20,22,24,-4],
    [30,28,27,26,-4],
    [25,30,35,-5],
    [40,-6]
]

# 그래프 위치, 말의 위치
horse = [
    [0,0],
    [0,0],
    [0,0],
    [0,0]
]

result = 0
dfs(0,dices[0],0,1)
print(result)
    
