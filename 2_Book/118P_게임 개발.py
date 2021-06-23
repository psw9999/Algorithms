n,m = map(int, input().split())

place = [[None]* n for i in range(n)]

a,b,cur = map(int,input().split())

cur_list = [(-1,0),(0,-1),(1,0),(0,1)]

for i in range(m) :
    place[i] = input().split()
    for j in range(n) :
        if place[i][j] == '0' :
            place[i][j] = 0
        else :
            place[i][j] = 2

def turn_left():
    global cur
    cur-=1
    if cur == -1 :
        cur = 3

place[a][b] = 1
result = 1

i=0
while(1) :
    turn_left()
    t_a,t_b = a+cur_list[cur][1],b+cur_list[cur][0]
    # 맵밖으로 나가는 경우  
    if t_a < 0 or t_b < 0 or t_a > (n-1) or t_b > (m-1) :
        i+=1
    # 바다 혹은 방문한 곳인 경우
    elif place[t_a][t_b] >= 1 :
        i+=1
    # 해당 방향으로 정상적으로 이동
    else :
        i = 0
        a,b = t_a, t_b
        place[t_a][t_b] += 1
        result += 1
    # 4 방향 모두 돌았는데 길이 없는 경우
    if i == 4 :
        t_a,t_b = a-cur_list[cur][1],b-cur_list[cur][0]
        if place[t_a][t_b] <= 1 :
            a,b = t_a, t_b
        else :
            break
        i = 0

print(result)

