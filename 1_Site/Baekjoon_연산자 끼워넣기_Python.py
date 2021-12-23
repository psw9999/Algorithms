
# 파이썬 음수 나눗셈시 값이 이상하게 출력됨. (ex : -5 // 3 = 2, -3 // 5 = 1)
# 원래는 값이 같은 경우를 제외하고는 +1을 하는 방법을 사용하였으나 문제가 계속 틀림.
# 파이썬에서 음수 // 양수 혹은 양수 // 음수 계산시 그냥 int(n1 / n2)로 사용하기
maxV = int(-1e9)
minV = int(1e9)

N = int(input())

numbers = list(map(int,input().split()))

sign = list(map(int,input().split()))

def bfs(cnt, value) :
    global N,maxV,minV,sign
    
    if cnt == N-1 :
        maxV = max(maxV, value)
        minV = min(minV, value)
        return
    
    if sign[0] > 0 :
        sign[0]-=1
        bfs(cnt+1, value + numbers[cnt+1])
        sign[0]+=1
    
    if sign[1] > 0 :
        sign[1]-=1
        bfs(cnt+1, value - numbers[cnt+1])
        sign[1]+=1

    if sign[2] > 0 :
        sign[2]-=1
        bfs(cnt+1, value * numbers[cnt+1])
        sign[2]+=1
        
    if sign[3] > 0 :
        sign[3]-=1
        # if value < 0 and abs(value) != numbers[cnt+1] :
        #     bfs(cnt+1, (value // numbers[cnt+1])+1)
        # else :
        #     bfs(cnt+1, value // numbers[cnt+1])
        bfs(cnt+1, int(value / numbers[cnt+1]))
        sign[3]+=1
        
bfs(0, numbers[0])
print(maxV)
print(minV)