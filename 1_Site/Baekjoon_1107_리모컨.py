import sys

input = sys.stdin.readline
global result

N = int(input().rstrip())
M = int(input().rstrip())
buttons = []
if M != 0:
    buttons = list(map(int, input().rstrip().split()))

result = int(1e9)
def dfs(cur, cnt) :
    global result

    if cnt != 0 :
        result = min(abs(N-cur)+cnt, result)
    
    if cnt >= 6 :
        return
    
    for btn in range(10) :
        if btn in buttons :
            continue
        dfs((cur*10)+btn, cnt+1)
    

dfs(0,0)
result = min(abs(N-100), result)

print(result)