# 1. DFS로 풀이하려는 느낌은 잡았는데 구현에 시간이 좀 걸렸음.
# 2. place[y][x]를 place[x][y]로 표현하여 오류가 발생했다.. 행렬의 x,y 개념을 잘 이해해야겠다.


def solution(places) :
    result = [1,1,1,1,1]
    for i in range(len(places)) :
        for j in range((len(places[i]))) :
            for e in range((len(places[i][j]))) : 
                if(places[i][j][e] == 'P') :
                    places[i][j] = places[i][j].replace('P','X',1)
                    if(dfs(e+1, j, 1, places[i]) or dfs(e, j+1, 1, places[i]) or dfs(e-1, j, 1, places[i])) :
                        result[i] = 0
                        break
            if(result[i] == 0) :
                break
            
    return result
            
def dfs(x,y,cnt,places) :
    if x <= -1 or y <= -1 or x >= 5 or y >= 5 or places[y][x] == 'X' :
        return 0
    if places[y][x] == 'P' :
        return 1
    if cnt == 2 :
        return 0

    return (dfs(x-1,y,cnt+1,places)+dfs(x+1,y,cnt+1,places)+dfs(x,y+1,cnt+1,places))