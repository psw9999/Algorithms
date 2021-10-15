# https://www.acmicpc.net/problem/1931
# 1. 종료시간이 시작시간보다 클 수는 없으므로 종료시간을 기준으로 sort를 진행하여 종료시간이 시작시간보다 큰 경우에 다시 종료시간을 갱신하도록 진행하였다.
# 2. (1,0), (1,1) 인 경우에 회의를 두번 진행할 수 있는데 (1,0)만 카운트로 세고 넘어가는 경우가 발생했다.
#    그래서 파이썬의 내장 sort 함수는 기존의 순서를 해치지 않고 정렬하는 것을 이용하여 다중조건정렬을 통해 해결하였다.

n = int(input())
m = []
for i in range(n) :
    m.append(tuple(map(int, input().split())))

# 내 소스
m.sort(key = lambda x : x[0])
m.sort(key = lambda x : x[1])
# 개선방식 (다중조건 정렬 활용)
#m.sort(key = lambda x: (x[0],x[1]))

min_value = 0
result = 0

for lst in m :
    if min_value <= lst[0] :
        min_value = lst[1]
        result +=1

print(result)

