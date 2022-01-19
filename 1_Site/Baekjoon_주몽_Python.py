import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
arr = list(map(int, input().split()))
arr.sort()
result = 0
left = 0
right = len(arr)-1

while True :
    total = arr[left] + arr[right]
    if total == M :
        result += 1
        left += 1
        right -= 1
    elif total > M :
        right -= 1
    else :
        left += 1

    if left >= right :
        break

print(result)