import math

def solution(n, k):
    value = ""
    temp = 1
    N = n
    prime_list = []
    # 1. 제곱값 구하기
    while True :
        if temp >= n :
            break
        else :
            temp *= k
    
    # 2. k진수의 값으로 변환
    while temp > 0 :
        if temp > N :
            value += '0'
        else :
            value += str((N//temp))
            N %= temp
        
        temp = temp // k
    
    # 3. 가장 왼쪽 비트가 0인 경우 제거
    if value[0] == '0' :
        value = value[1:]
    
    # 4. P 나누기
    temp = value.split('0')
    maxV = 1
    for prime in temp :
        if prime != '' :
            t = int(prime)
            maxV = max(maxV, t)
            prime_list.append(t)
    
    result = 0
    for prime in prime_list :
        if prime != 1 and is_prime_number(prime) :
            result += 1

    return result

#소수 판별 함수
def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어 떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True
            
    