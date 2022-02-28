
import sys
input = sys.stdin.readline
sys.setrecursionlimit(3000)

def dfs(y,x,cnt) :
    global visited, board, DP, maxV, N, M
    #print(y,x,cnt)
    dice = board[y][x]
    cnt += 1
    result = 0
    
    for my,mx in move :
        dy,dx = y + (my*dice), x + (mx*dice)
        
        # 맵 밖으로 벗어나거나 도착 지역이 구멍인 경우
        if dy < 0 or dx < 0 or dy >= N or dx >= M or board[dy][dx] == 0 :
            continue
        # 방문하려는 곳이 DP에 더 큰 값이 있는 경우, 다시 방문하여 진행하는 것이므로 필요 없음.
        if cnt <= DP[dy][dx] :
            continue
        # 방문한 곳을 재방문 -> 무한 루프를 돌고 있다는 뜻으로 -1 리턴
        if visited[dy][dx] == True :
            return -1
        
        DP[dy][dx] = cnt
        visited[dy][dx] = True
        temp = dfs(dy,dx,cnt)
        if temp == -1 :
            return temp
        result = max(temp, result)
        visited[dy][dx] = False
    
    return max(cnt,result)

        
N,M = map(int,input().rstrip().split())
maxV = int(1e9)
move = [(1,0),(0,1),(-1,0),(0,-1)]
board = []
for i in range(N) :
    temp = list(input().rstrip())
    for i,t in enumerate(temp) :
        if t == 'H' :
            temp[i] = 0
        else :
            temp[i] = int(t)
    board.append(temp)
visited = [[[False] for _ in range(M)] for _ in range(N)]
DP = [[0 for _ in range(M)] for _ in range(N)]

temp = dfs(0,0,0)
print(temp)