from collections import deque

N,K = map(int,input().split())

result_time = 10e6
result_cnt = 0
visited = [[10e6,0]] * (100001)
visited[N] = [0,1]
queue = deque()
queue.append((N,0))

def search(Loc, Time, cnt) :
    global K, result_time, result_cnt, visited
    if Loc == K :
        if Time < result_time : 
            result_time = Time
            result_cnt = cnt
        elif Time == result_time :
            result_cnt += cnt
    
    else :
        if Loc > 100000 or Loc < 0 :
            return
        if Time >= result_time or Time > visited[Loc][0]:
            return
        elif Time < visited[Loc][0] :
            queue.append((Loc,Time))
            visited[Loc] = [Time,cnt]
        else :
            visited[Loc][1] += cnt

if N >= K :
    print(N-K)
    print(1)

else :
    while queue :
        loc, time = queue.popleft()
        search(loc+1,time+1, visited[loc][1])
        search(loc-1,time+1, visited[loc][1])
        search(loc*2,time+1, visited[loc][1])
              
    print(result_time)
    print(result_cnt)
