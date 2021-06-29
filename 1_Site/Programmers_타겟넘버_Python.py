# 1. 코드의 가독성이 떨어지는 것 같음.
# 2. 노드의 루트가 0부터 시작하는 것이 코드의 작성과 이해하는데 도움을 줄 것 같음.

result = 0

def solution(numbers, target):
    global result
    result = 0
#    target *=-1
#    calcul(numbers,target,0,1)
#    calcul(numbers,target,0,-1)
    calcul(numbers,target,0,0)
    return result

#def calcul(numbers,target,n,sign) :
# 매개 변수 차례대로 주어진 숫자, 목표 값, 인덱스 카운트, 현재까지 더해진(뺀) 값이다.
def calcul(numbers,target,n,value) :
    global result
    nums_len = len(numbers)
    if(n == nums_len and target == value) :
        result +=1
        return
    if(n==nums_len) :
        return

    calcul(numbers,target,n+1,value+numbers[n])
    calcul(numbers,target,n+1,value-numbers[n])
    # if(n < len(numbers)) :
    #     target += numbers[n]*sign
    #     n+=1
    #     if n >= len(numbers) :
    #         if target == 0 :
    #             result+=1
    #     else :
    #         calcul(numbers,target,n,1)
    #         calcul(numbers,target,n,-1)