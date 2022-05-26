import heapq, sys
from collections import defaultdict

input = sys.stdin.readline

# 테스트 케이스
T = int(input())

result = []
for _ in range(T) :
    # 건물의 갯수 N , 건물간의 건설순서 규칙 K
    N,K = map(int, input().rstrip().split())
    # 건물 건설 시간
    times = list(map(int, input().rstrip().split()))
    child = defaultdict(list)
    parent = defaultdict(list)
    for _ in range(K) :
        start, end = map(int, input().rstrip().split())
        parent[end-1].append(start-1)
        child[start-1].append(end-1)
    visited = [False] * N
    completed = [False] * N
    # 승리를 위해 건설되어야 하는 건물
    W = int(input()) - 1

    cur_time = 0
    queue = []
    for i in range(N) :
        if len(parent[i]) == 0 :
            heapq.heappush(queue, [times[i],i])
            visited[i] = True
    
    while queue :
        time, building = heapq.heappop(queue)
        if time < 0 :
            time = 0
        completed[building] = True
        cur_time += time
        # 탈출 조건 : 승리를 위해 건설되어야 하는 건물 완성시 승리
        if building == W :
            result.append(cur_time)
            break

        # 현재 지을 수 있는 건물에 시간 빼주기
        for i in range(len(queue)) :
            queue[i][0] -= time
        
        for p in child[building] :
            if visited[p] == True :
                continue
            flag = True
            for c in parent[p] :
                if completed[c] == False :
                    flag = False
                    break 
            if flag :
                heapq.heappush(queue, [times[p],p])
                visited[p] = True

#print(result)
for r in result :
    print(r)
