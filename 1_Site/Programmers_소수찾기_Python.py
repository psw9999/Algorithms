# 1. 특정 수가 소수인지 판단하는 방법은 2에서 제곱근까지 나눠주는 에라토스테네스의 체라는 방법을 사용하면 쉽게 풀 수 있다.
# 2. 제곱근을 구하는 함수는 sqrt(숫자)를 사용하여 구할 수 있다.
# 3. 수를 조합하여 같은 숫자가 나올 수 있으므로 중복을 허용하지 않는 set 자료구조를 사용한다.
# 4. 리스트의 내의 숫자들을 permutations()를 이용해 순열 조합 시킬 수 있다.

from itertools import permutations

def solution(numbers) :
    result = 0
    # 문자열인 numbers를 하나씩 잘라 리스트에 저장함.
    nums =  [n for n in numbers]
    arr = []
    set_arr = set()
    # permutations(순열)을 사용해 i개씩 묶어지는 list를 생성
    for i in range(1, len(nums)+1) :
        arr = list(permutations(nums,i))
        for j in range(len(arr)) :
            set_arr.add(int(''.join(arr[j])))
    
    for n in set_arr :
        flag = True
        if n == 0 or n == 1 : 
            continue
        else :
            for i in range(2, int(math.sqrt(n))+1) :
                if n % i == 0 :
                    flag = False
                    break
            if flag == True :
                result+=1
        