import sys

# (y,x)
move = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
input = sys.stdin.readline
N,M,K = map(int, input().rstrip().split())
graph = [[5 for _ in range(N)] for _ in range(N)]
tree_graph = [[[] for _ in range(N)] for _ in range(N)]
robot_graph = []
for _ in range(N) :
    robot_graph.append(list(map(int, input().rstrip().split())))

for _ in range(M) :
    y,x,z =  map(int, input().rstrip().split())
    tree_graph[y-1][x-1].append(z)
        

for _ in range(K) :
    # 죽은 나무를 저장하는 맵
    deadTree = [[0 for _ in range(N)] for _ in range(N)]
    
    # 나이 작은 나무 순으로 리스트 sort
    for y in range(N) :
        for x in range(N) :
            tree_graph[y][x].sort()
    
    # 봄
    for y in range(N) :
        for x in range(N) :
            result = []
            for tree in tree_graph[y][x] :
                # 죽은 나무의 양분을 절반 더함.
                if tree > graph[y][x] :
                    deadTree[y][x] += (tree//2)
                # 자신 나이 만큼 양분을 먹고, 나이 1 증가
                else :
                    graph[y][x] -= tree
                    result.append(tree+1)
            # 살아남은 나무로 tree_graph 갱신
            tree_graph[y][x] = result
                

    # 여름
    # 봄에 죽은 나무의 양분을 더해줌.
    for y in range(N) :
        for x in range(N) :
            graph[y][x] += deadTree[y][x]
    
    # 가을
    # 번식하는 나무의 나이가 5의 배수이면 인접하는 8개의 칸에 나이가 1인 나무가 발생함.
    for y in range(N) :
        for x in range(N) :
            for tree in tree_graph[y][x] :
                if tree % 5 == 0 and tree != 0 :
                    for my,mx in move :
                        dx,dy = x+mx, y+my
                        if dx < 0 or dy < 0 or dx >= N or dy >= N :
                            continue
                        tree_graph[dy][dx].append(1)
    
    # 겨울
    # 땅에 양분 추가
    for y in range(N) :
        for x in range(N) :
            graph[y][x] += robot_graph[y][x]

result = 0
# 살아있는 나무의 수
for y in range(N) :
    for x in range(N) :
        result += len(tree_graph[y][x])
print(result)
                