
import sys

input = sys.stdin.readline

N,C = map(int,input().rstrip().split())
home = []

for _ in range(N) :
    home.append(int(input().rstrip()))
home.sort()

#right, left = home[-1], home[0]
# 두 집 사이의 최소 거리, 최대 거리
left, right = 1, home[-1] - home[0]
result = 0

while right >= left :
    mid = (right + left) // 2
    count = 1
    index = 0
    
    for i in range(1, len(home)) :
        if (home[i] - home[index]) >= mid :
            index = i
            count += 1
        
    if count >= C :
        result = max(result, mid)
        left = mid + 1
    
    else :
        right = mid - 1

print(result)
                
            