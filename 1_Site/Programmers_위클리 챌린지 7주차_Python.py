def solution(enter, leave):
    result = [0 for i in range(len(enter))]
    temp = []
    j = 0

    for i in enter :

        temp.append(i)
        result[i-1] += len(temp)-1
        for x in range(len(temp)-1) :
            result[temp[x]-1] += 1

        while leave[j] in temp :
            temp.remove(leave[j])
            if j < len(leave)-1 :
                j+=1

    return result