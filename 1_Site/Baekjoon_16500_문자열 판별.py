import sys

input = sys.stdin.readline
target = input().rstrip()
N = int(input().rstrip())
str_list = []
for _ in range(N) :
    str_list.append((input().rstrip()))

dp = [0] * (len(target) + 1)
dp[0] = 1

for i in range(1, len(target)+1) :
    for s in str_list :
        
        if len(s) > i :
            continue
        
        if dp[i-len(s)] == 1 and s == target[i-len(s):i] :
            dp[i] = 1
            break
if dp[len(target)] == 1 :
    print(1)
else :
    print(0)