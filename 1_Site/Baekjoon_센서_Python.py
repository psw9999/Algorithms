
import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
arr = list(map(int, input().split()))
arr.sort()

if K >= N :
    print(0)
    exit(0)

distance = []
result = 0

for i in range(len(arr)-1) : 
    #print(arr[i+1] - arr[i])
    distance.append(arr[i+1] - arr[i])

distance.sort(reverse=True)
for d in distance[K-1:] :
    result += d

print(result)