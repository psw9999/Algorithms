import sys

input = sys.stdin.readline

N,attack = map(int, input().rstrip().split())

maxH = 0
curH = 0

for _ in range(N) :
    t,a,h = map(int, input().rstrip().split())
    
    # 던전
    if t == 1 :
        if h % attack == 0 :
            curH -= (a * ((h//attack)-1))
        else :
            curH -= (a * ((h//attack)))
        #print(curH)
        maxH = max(maxH, -curH)
    
    # 힐링
    else :
        attack += a
        curH = min(0, (curH+h))

print(maxH+1)