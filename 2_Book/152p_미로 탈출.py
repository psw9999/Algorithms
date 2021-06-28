from collections import deque

n,m = map(int,input().split())

maze = []

for i in range(n) :
    maze.append(list(map(int,input())))

# 상하좌우
x_list = [0,0,-1,1]
y_list = [-1,1,0,0]


def bfs(x,y) :
    queue = deque()
    queue.append((x,y))
    # 시작점을 재방문하는 것을 방지하기 위해 2로 초기화
    maze[x][y] = 2

    # 큐가 존재할 때 까지
    while queue :
        x,y = queue.popleft()
        for i in range(4) :
            tx = x+x_list[i]
            ty = y+y_list[i]
            if tx < 0 or ty < 0 or tx > (m-1) or ty > (n-1) :
                continue
            # 괴물이 있는 경우 무시
            if maze[tx][ty] == 0 :
                continue
            if maze[tx][ty] == 1 :
                maze[tx][ty] = maze[x][y] + 1
                queue.append((tx,ty))

    return (maze[n-1][m-1]-1)

print(bfs(0,0))

            


