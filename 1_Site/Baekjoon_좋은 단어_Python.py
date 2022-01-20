
import sys
input = sys.stdin.readline

N = int(input())
cnt = 0
result = 0

while cnt < N :
    word = list(input().rstrip())
    stack = []
    
    for w in word :
        if len(stack) == 0 :
            stack.append(w)
        else :
            if stack[-1] == w :
                stack.pop()
            else :
                stack.append(w)
    
    if len(stack) == 0 :
        result += 1
    cnt += 1
print(result)