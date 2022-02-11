
import sys

input = sys.stdin.readline

N,S = map(int, input().rstrip().split())
numbers = list(map(int,input().rstrip().split()))

result = int(1e9)
total = 0
length = -1
for i in range(N) :
    total += numbers[i]
    length += 1
    if total >= S :
        for j in range(i-length,i) :
            if (total - numbers[j]) >= S :
                total -= numbers[j]
                length -= 1
            else :
                break
        result = min(result,length+1)
        total -= numbers[i-length]
        length -= 1

if result == int(1e9) :
    print(0)
else :
    print(result)