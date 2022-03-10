# 락 상태 확인
def checkLock(graph,lock_start,lock,L) : 
    for i in range(L) :
        for j in range(L) :
            if graph[lock_start + i][lock_start + j] != 1:
                # 자물쇠 중앙쪽 다시 원래대로 초기화
                for i in range(L) :
                    for j in range(L) :
                        graph[lock_start + i][lock_start + j] = lock[i][j]
                return False
    return True

def solution(key, lock):
    K = len(key)
    L = len(lock)
    
    # 자물쇠와 키를 넣은 맵 생성
    graph = [[0 for _ in range(L + (K * 2) - 2)] for _ in range(L + (K * 2) - 2)]
    G = len(graph)
    
    # 키를 시계방향으로 회전하기
    keys = [key]
    for k in range(3) : 
        temp = [[0 for _ in range(K)] for _ in range(K)]
        temp_key = keys[k]
        for i in range(K) :
            for j in range(K) :
                temp[i][j] = temp_key[K-1-j][i]
        keys.append(temp)
        
    # 중앙에 자물쇠 넣기
    lock_start = (len(graph) // 2) - (L // 2)
    for i in range(L) :
        for j in range(L) :
            graph[lock_start + i][lock_start + j] = lock[i][j]
    
    # 맵에 키 넣기
    for i in range(G-K+1) :
        for j in range(G-K+1) :
            for key in keys :
                for k1 in range(len(key)) :
                    for k2 in range(len(key[0])) :
                        graph[i + k1][j + k2] += key[k1][k2]
                flag = checkLock(graph,lock_start,lock,L)
                if flag == True :
                    return True
    return False