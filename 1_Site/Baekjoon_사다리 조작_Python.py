
from itertools import combinations, permutations
import sys

input = sys.stdin.readline

# 노드 탐색
def search(num) :
    global bridge, H
    cur = num
    
    for time in range(1, H+1) :
        temp = cur
        if cur > 1 :
            if bridge[cur-1][time] :
                temp -= 1
                
        if cur < N :
            if bridge[cur][time] :
                temp += 1
        cur = temp
        
    if cur == num :
        return True

    return False

def makePermutation(number) :
    global perm
    for p in list(combinations(perm, number)) :
        flag = False
        for l in range(len(p)-1) :
            for t in range(l, len(p)-1) :
                if p[t][1] == p[t+1][1] :
                    if (p[t][0]+1) == p[t+1][0] or (p[t][0]-1) == p[t+1][0] :
                        flag = True
                        break
            
        if not flag :
            temp = False
            for b,a in p :
                bridge[b][a] = 1

            for i in range(1,N+1) :
                if not search(i) :
                    temp = True
                    break

            if not temp :
                return True

            for b,a in p :
                bridge[b][a] = 0

    if number == 0 :
        temp = False
        for i in range(1,N+1) :
            if not search(i) :
                temp = True
                break
        
        if not temp :
            return True  
    
    return False      
            
N,M,H = map(int,input().rstrip().split())

if M == 0 :
    print(0)
    exit()

base = []
perm = []
bridge = [[0] * (H+1) for _ in range(N+1)]

# a : 시간, b : 세로선
for _ in range(M) :
    a,b = map(int, input().rstrip().split())
    bridge[b][a] = 1
    base.append((b,a))

# 조합용 리스트 만들기
# 세로선
for i in range(1, N) :
    # 시간
    for j in range(1, H+1) :
        flag = False
        for b,a in base :
            if j == a :
                if (i-1) == b or i == b or (i+1) == b:
                    flag = True
                    break
        if not flag :
            perm.append((i,j))

print(perm)

for i in range(4) :
    if makePermutation(i) :
        print(i)
        exit()

print(-1)

