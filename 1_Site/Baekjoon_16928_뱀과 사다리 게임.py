import sys
import heapq
input = sys.stdin.readline
MAX = int(1e9)
visited = [MAX] * 101
visited[1] = 0

# 주사위 굴린 수, 현재 위치
queue = [(0,-1)]
# 사다리
radders = dict()
# 뱀
# snakes = dict()

N,M = map(int, input().rstrip().split())
for _ in range(N+M) :
    start, end = map(int, input().rstrip().split())
    radders[start] = end

# for _ in range(M) :
#     start, end = map(int, input().rstrip().split())
#     snakes[start] = end

while queue :
    count, loc = heapq.heappop(queue)
    loc = (-loc)

    # 100에 도착했는가?
    if loc == 100 :
        print(count)
        break

    # 뱀이나 사다리로 이동 가능한 영역이 있는지
    if loc in radders :
        move_loc = radders[loc]
        if count < visited[move_loc] :
            visited[move_loc] = count
            heapq.heappush(queue, (count, -move_loc))
    
    # if loc in snakes : 
    #     move_loc = snakes[loc]
    #     if count < visited[move_loc] :
    #         visited[move_loc] = count
    #         heapq.heappush(queue, (count, -move_loc))
    else :
        for i in range(1,7) :
            move_loc = loc + i
            if move_loc > 100 :
                break
            if (count+1) < visited[move_loc] :
                visited[move_loc] = count+1
                heapq.heappush(queue, (count+1, -move_loc))
