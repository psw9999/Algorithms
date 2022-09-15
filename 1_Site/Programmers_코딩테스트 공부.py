def solution(alp, cop, problems):
    INF = int(1e9)
    alp_max = 0
    cop_max = 0
    
    for alp_req, cop_req, _, _, _ in problems :
        alp_max = max(alp_req, alp_max)
        cop_max = max(cop_req, cop_max)
    
    DP = [[INF for _ in range(cop_max+1)] for _ in range(alp_max+1)]
    # 초기 알고력과 코딩력이 맥스값보다 큰 경우가 있음.
    alp = min(alp, alp_max)
    cop = min(cop, cop_max)
    DP[alp][cop] = 0
    
    for i in range(alp, alp_max+1) :
        for j in range(cop, cop_max+1) :
            if i+1 <= alp_max :
                DP[i+1][j] = min(DP[i+1][j], DP[i][j]+1)
            if j+1 <= cop_max :
                DP[i][j+1] = min(DP[i][j+1], DP[i][j]+1)
            
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems : 
                if i >= alp_req and j >= cop_req :
                    tmp_alp = min(i+alp_rwd, alp_max)
                    tmp_cop = min(j+cop_rwd, cop_max)
                    
                    DP[tmp_alp][tmp_cop] = min(DP[tmp_alp][tmp_cop], DP[i][j] + cost)
                    
    return DP[-1][-1]