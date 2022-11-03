import sys
from collections import deque

input = sys.stdin.readline
N = int(input().rstrip())
stack_balls = list(input().rstrip())
result = int(1e9)
deque_balls = deque(stack_balls[:])

first = stack_balls.pop()
while stack_balls :
    if stack_balls[-1] != first :
        break
    stack_balls.pop()
result = min(result, stack_balls.count('R'), stack_balls.count('B'))

first = deque_balls.popleft()
while deque_balls :
    if deque_balls[0] != first :
        break
    deque_balls.popleft()
result = min(result, deque_balls.count('R'), deque_balls.count('B'))

print(result)

