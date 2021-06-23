def solution(numbers):
    result_set = set()
    for i in range (len(numbers)-1) :
        for j in range (i+1, len(numbers)) :
            result_set.add(numbers[i]+numbers[j])
    result = list(result_set)
    result.sort()
    return result
