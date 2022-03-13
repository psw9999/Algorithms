def solution(N, number):
    DP = []
    
    for i in range(1, 9) :
        number_set = set()
        number_set.add(int(str(N) * i))
        
        for j in range(i-1) :
            for first in DP[j] :
                for second in DP[-j-1] :
                    number_set.add(first + second)
                    number_set.add(first - second)
                    number_set.add(first * second)
                    if second != 0 :
                       number_set.add(first // second)
        
        if number in number_set :
            return i
        
        DP.append(number_set)
    
    return -1