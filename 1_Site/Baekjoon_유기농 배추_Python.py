# 재귀함수를 이용할시 런타임에러 발생 -> 너무 깊은 곳까지 탐색하게 되므로 (반복문을 이용한 dfs로 수정)
t = int(input())
move = [(1,0),(-1,0),(0,1),(0,-1)]
stack = []
result = []

for temp in range(t) :
    m,n,k = list(map(int,input().split()))
    answer = 0

    # 이차원 배열 생성법 잘 알아두기
    array = [[0]*m for i in range(n)]

    for i in range(k) :
        x,y = map(int,input().split())
        array[y][x] = 1
    
    for y in range(len(array)) :
        for x in range(len(array[y])) :
            if array[y][x] == 1 :
                for mt in move :
                    stack.append((x+mt[0], y+mt[1]))
                while stack :
                    tx, ty = stack.pop()
                    if tx < 0 or ty < 0 or tx > (m-1) or ty > (n-1) :
                        continue
                    if array[ty][tx] == 0 :
                        continue
                    else :
                        array[ty][tx] = 0
                        for mt in move :
                            stack.append((tx+mt[0], ty+mt[1]))
                answer += 1
    result.append(answer)

for r in result :
    print (r)
    