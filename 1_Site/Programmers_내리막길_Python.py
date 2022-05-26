import heapq

def bit_mask(dir, traps_index, node, flag):
    if flag == 1: # 현재 방향
        return (1 & (dir >> traps_index[node]))
    else: # 트랩을 밟아서 다음 상태 변경
        return dir ^ (1 << traps_index[node])

def solution(n, start, end, roads, traps):
    answer = 0
    MAX = int(1e9)
    # 비트마스크이므로 2의 제곱만큼 DP 맵 생성 (트랩은 최대 10개이므로 2 ** 10 = 1024)
    DP = [[MAX for _ in range(n+1)] for _ in range(2**len(traps))]
    # 트랩의 노드가 몇번 인덱스인지 판별하기 위한 dict 변수
    trapDict = { node : i  for i,node in enumerate(traps) }
    queue = []
    graph = [[] for _ in range(n+1)]

    for road in roads:
        s, e, cost = road
        # 0: 정방향
        graph[s].append([e, cost, 0])
        # 1: 역방향
        graph[e].append([s, cost, 1])

    heapq.heappush(queue,(0, start, 0))
    DP[0][start] = 0
   
    while queue:
        # 노드까지 이동하는데 걸린 시간, 현재 노드, 방향?
        nowCost, nowNode, nowDir = heapq.heappop(queue)

        if nowNode == end :
            answer = nowCost
            break
            
        if DP[nowDir][nowNode] < nowCost:
            continue
            
        for nextNode, cost, dir in graph[nowNode]:
            nextDir = nowDir
            cur_flag = 0
            # 현재 노드가 트랩일 때
            if nowNode in traps :
                # 다음 노드도 트랩인경우
                if nextNode in traps:
                    prev = bit_mask(nowDir, trapDict, nowNode, 1)
                    nxt = bit_mask(nowDir, trapDict, nextNode, 1)
                    '''
                       prev       nxt    result
                     1(역방향)   1(역방향)  0(정방향)
                     1(역방향)   0(정방향)  1(역방향)
                     0(정방향)   1(역방향)  1(역방향)
                     0(정방향)   0(정방향)  0(정방향)
                    '''
                    cur_flag = (prev + nxt) % 2
                    next_state = bit_mask(state, traps_index, next_node, 2)
                    
                # 다음 노드는 트랩이 아닌 경우
                else:
                    cur_flag = bit_mask(state, traps_index, cur_node, 1)
                    
            # 현재 노드가 트랩이 아닌 경우
            else:
                # 다음 노드가 트랩일 때
                if next_node in traps:
                    cur_flag = bit_mask(state, traps_index, next_node, 1)
                    next_state = bit_mask(state, traps_index, next_node, 2)

                # 다음 노드는 트랩이 아닌 경우
                else:
                    cur_flag = 0
                    
            if cur_flag == flag:
                if dp[next_state][next_node] > cur_time + cost:
                    dp[next_state][next_node] = cur_time + cost
                    heapq.heappush(node_list, (dp[next_state][next_node], next_node, next_state))

    return answer