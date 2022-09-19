
import sys

input = sys.stdin.readline

S = input().rstrip()
explosion = input().rstrip()
e = len(explosion)
stack = []

for s in S :
    stack.append(s)
    if explosion[-1] == s and "".join(stack[-e:]) == explosion :
        del stack[-e:]

if len(stack) == 0 :
    print("FRULA")
else :
    print("".join(stack))