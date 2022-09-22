
import sys

input = sys.stdin.readline

N = int(input().rstrip())
tops = list(map(int, input().rstrip().split()))
result = [0 for _ in range(N)]
stack = []

i = len(tops) - 1
while tops :
    current = tops.pop()
    
    # 스택의 탑들과 차례대로 비교
    while len(stack) > 0 :
        j, height = stack[-1]
        if current >= height :
            stack.pop()
            result[j] = i+1
        else :
            break
    stack.append((i, current))
    i -= 1

print(" ".join(list(map(str, result))))
            