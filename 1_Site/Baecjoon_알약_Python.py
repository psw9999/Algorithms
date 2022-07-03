
import sys

input = sys.stdin.readline

def recursion(w,h) :
    global DP
    if w > h :
        return 0
    
    if not DP[w][h] :
        DP[w][h] = recursion(w-1,h) + recursion(w,h-1)
        return DP[w][h]
    
    else :
        return DP[w][h]

DP = [[0] * 31 for _ in range(31)]
DP[1][1] = 1
for i in range(31) :
    DP[0][i] = 1

result = []
while True :
    temp = int(input())
    if not temp :
        for r in result :
            print(r)
        break
    result.append(recursion(temp-1,temp))
