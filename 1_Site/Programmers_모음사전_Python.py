def solution(word):
    dic = {'A' : 0, 'E' : 2, 'I' : 3, 'O' : 4, 'U' : 5}
    result = 0
    
    for i in range(len(word)) :
        temp = dic[word[i]]
        if temp == 0 :
            result+=1
        else :
            for j in range(5-i) :
                if j == 0 :
                    result += temp
                else :
                    result += (5 ** j) * (temp-1)
        
    return result