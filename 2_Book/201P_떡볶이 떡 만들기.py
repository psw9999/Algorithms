
# 파라메트릭 서치 사용
# 범위 내에서 조건을 만족하는 가장 큰 값을 찾으라는 최적화 문제 

n,m = list(map(int, input().split(' ')))
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while(start <= end) :
    total = 0
    mid = (start+end) // 2
    for i in array :
        if i > mid :
            total += mid - i


    if total < m : 
        end = mid - 1
    else :
        result = mid
        start = mid + 1

    print(result)
        
     