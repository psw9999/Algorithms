def solution(A,B):
    result = 0
    A.sort(reverse = True)
    B.sort()
  
    for i in range(len(A)) :
        result += A[i] * B[i]
    
    return result