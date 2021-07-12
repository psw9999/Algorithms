# 코드리뷰
# 1. 구현방식
# 1.1. speeds의 값을 1번씩 늘려가며 구하는 방식은 비효율적이라 생각하여서 100에서 현재 진행률을 뺀 값과 진행속도를 나눈 값을 곱하여 곧바로 0번째 인덱스값이 100 이상이 될 수 있도록 하였다.
# 1.2. deque를 사용해 첫번째 진행률이 100%를 초과하면 popleft()를 통해 첫번째 리스트 값을 제한다. 이것이 연속적으로 되면 반복하고 아니면, 1.1로 돌아가 연산을 수행한다.

# 3. 시간복잡도
# 3.1. 내가 한 방식은 최악의 경우([99,98,97,96,..],[1,1,1,1,..]) 원소가 하나씩 진행될 때마다 리스트의 끝까지 연산이 진행되어야 함. (n+(n-1)+(n-2)+...) = N*(N-1)/2 = O(N2)
# 3.2. 곱해진 값은 뒷부분에도 동일하게 적용되므로 뒷부분은 곱하지 않고 하나씩 적용하여 진행하면 시간 복잡도가 O(n)으로 계산될 것 같음.

from collections import deque

def solution(progresses, speeds):
    result = []
    progresses_queue = deque(progresses)
    speeds_queue = deque(speeds)
    
    while progresses_queue :
        remainder = 100 - progresses_queue[0]
        quotient = remainder // speeds_queue[0]
        if remainder % speeds_queue[0] != 0 :
            quotient += 1

        Flag = 1
        cnt = 0
        for i in range(len(progresses_queue)) :
            cur = i - cnt
            progresses_queue[cur] = progresses_queue[cur] + (speeds_queue[cur] * quotient)
            if Flag :
                if progresses_queue[cur] >= 100 :
                    progresses_queue.popleft()
                    speeds_queue.popleft()
                    cnt += 1
                else :
                    Flag = 0

        if(cnt!=0):   
            result.append(cnt)

    return result
            