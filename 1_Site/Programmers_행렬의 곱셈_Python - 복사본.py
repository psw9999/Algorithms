def solution(arr1, arr2) :
    result = [ [0]*len(arr2[0]) for _ in range(len(arr1)) ]
    
    for i in range(len(arr1)) :
        for j in range(len(arr2[0])) :
            temp = 0
            for z in range(len(arr1[0])) :
                temp += arr1[i][z] * arr2[z][j]
            result[i][j] = temp
    
    return result