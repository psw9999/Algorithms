


def binary_search(array, target, start, end) :
    mid = (start+end)//2

    if array[mid] == target :
        return mid
    elif start == end : 
        return None
    elif array[mid] > target : 
        return binary_search(array, target, start, mid-1)
<<<<<<< HEAD
    else : 
=======
    elif array[mid] < target : 
>>>>>>> db39e03d1a9cc5763594aa5379ba2c667b16de1c
        return binary_search(array, target, mid+1, end)
    

# 이진 탐색의 조건 : 반드시 리스트 내부가 먼저 정렬되어 있어야 한다.
# 원소 개수 : n, 찾을 값 : target 입력
n, target = list(map(int, input().split()))

# 전체 원소 입력받기
array = list(map(int, input().split()))

result = binary_search(array, target, 0 , n-1)

if(result == None) :
    print("해당하는 값이 없습니다.")

else :
    print(n+1+"번째 자리에 존재합니다.")
