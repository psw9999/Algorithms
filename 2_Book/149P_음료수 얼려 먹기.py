# 1. 상하좌우로 얼음을 탐색하는게 핵심
# 2. 탐색한 노드가 얼음인 경우 그 노드의 상하좌우를 체크하여 이어진 얼음인지 체크한다.
# 3. 이 때, 재귀함수를 사용하여 한 노드에서 발생시 연속적으로 발생하게 하고 복귀를 할 수 있는 재귀함수를 사용하는 것이 중요함.

n, m = map(int,input().split())

ice = []
for i in range(n) :
    ice.append(list(map(int,input())))

def dfs(x,y) :
    if x <= -1 or x >= n or y <= -1 or x >=m :
        return False
    
    #현재 노드가 방문하지 않은 얼음이라면,
    if ice[x][y] == 0 :
        # 방문한 것으로 처리함
        ice[x][y] = 1
        # 사방면을 방문하여 
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False

result = 0
for i in range(n) :
    for j in range(m):
        if dfs(i,j) == True :
            result +=1
