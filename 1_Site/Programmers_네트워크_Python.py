from collections import deque

def solution(n, computers):
    result = 0
    visited = [0]*n
    for i in range(n) :
        for j in range(n) :
            if computers[i][j] :
                queue = deque()
                queue.append(j)
                while queue :
                    y = queue.popleft()
                    for x in range(len(computers[y])) :
                        if computers[y][x] and visited[x] == 0 :
                            visited[x] = 1
                            queue.append(x)
                        computers[y][x] = 0
                result += 1
                
    return result