
import sys

input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().rstrip().split()))
arr.sort()

result = set()
for i in range(N) :
    for j in range(i+1,N) :
        target = arr[i] + arr[j]
        temp = arr[:i] + arr[i+1:]
        left, right = 0, len(temp)
        mid = (left + right) // 2
        while left <= right : 
            if temp[mid] == target : 
                if temp[mid] != temp[i] and temp[mid] != temp[j] :
                    result.add(mid)
                    break

            if target > temp[mid] :
                left = mid + 1
            
            elif target < temp[mid] :
                right = mid - 1

            mid = (left + right) // 2

print(len(result))