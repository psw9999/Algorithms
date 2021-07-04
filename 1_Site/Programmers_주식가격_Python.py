# 코드리뷰
# 1-1. 뒷부분 상태부터 탐색하여 떨어지지 않은 구간이 얼마인지 먼저 탐색하도록 함. 왜냐하면 앞부분의 주식가격이 이 데이터를 활용해 시간복잡도를 크게 줄일 수 있기 때문이다.
# 1-2. 요구하는 출력형식을 만족하기 위해 deque의 appendleft함수를 사용함.
# 2-1. deque 상태로 return시 'TypeError: Object of type dict_keys is not JSON serializable'이라는 에러가 발생함
# 2-2. 왜냐면 deque를 출력시 deque([1,2,3]) 형식으로 출력되기 때문이다.
# 2-3. 그러므로 반드시 deque를 list함수를 통해 변환과정을 거쳐 return하도록 해야함, list 함수의 시간복잡도는 아마도 O(n)으로 예상
# 3. 시간복잡도 : 여러 경우 고려 시 거의 O(n)으로 추정됨.(ex : 1,2,1,2,1,2,1,2,...), (ex: 1,2,3,4,5,6,7...)

from collections import deque

def solution(prices):
    length = len(prices)
    result = deque()
    result.appendleft(0)
    for i in range(length-2,-1,-1) :
        j = i
        cnt = 0
        while result[cnt] != 0 :
            if prices[j] > prices[j+cnt+1] :
                break
            else :
                cnt += result[cnt]
        result.appendleft(cnt+1)
    
#    return result
    return list(result)