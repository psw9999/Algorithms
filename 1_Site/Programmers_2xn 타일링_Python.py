def solution(n):
    DP = [0] * (60001)
    DP[1] = 1
    DP[2] = 2
    
    for i in range(3,n+1) :
        DP[i] = (DP[i-1] + DP[i-2]) % 1000000007
    
    return DP[n]