
import sys
input = sys.stdin.readline

target = int(input().rstrip())
M,N = map(int,input().rstrip().split())

pizzaA = []
for _ in range(M) :
    pizzaA.append(int(input().rstrip()))

pizzaB = []
for _ in range(N) :
    pizzaB.append(int(input().rstrip()))
    
result = 0
def getPizza(pList, cnt) :
    global result,target
    frac = dict()
    for i in range(cnt) :
        if pList[i] > target :
            continue
        elif pList[i] == target :
            result += 1
            continue
        temp = pList[i]
        
        if not temp in frac :
            frac[temp] = 1
        else :
            frac[temp] += 1

        for j in range(1,cnt-1) :
            t = (i+j)%cnt
            temp += pList[t]
            
            if temp > target :
                break
            elif temp == target :
                result += 1
                break
            
            if not temp in frac :
                frac[temp] = 1
            else :
                frac[temp] += 1
                
    return frac

frac_a = getPizza(pizzaA,M)
frac_b = getPizza(pizzaB,N)

for a in frac_a :
    tempTarget = target - a
    
    if tempTarget in frac_b :
        result += frac_a[a] * frac_b[tempTarget]

print(result)